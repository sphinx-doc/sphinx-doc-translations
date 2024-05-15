#!/usr/bin/env python3
"""
Locks obsolete resources in a Transifex project,
then remove them after 3 days remove them if still locked.

SPHINXINTL_TRANSIFEX_ORGANIZATION_NAME and SPHINXINTL_TRANSIFEX_PROJECT_NAME
environment variables must be set.
"""

import os
import re
import argparse
import configparser
import dateutil.parser
import dateutil.utils
from datetime import datetime
from transifex.api import transifex_api


def printmsg(type, message):
    """Format message in case it is being run in GitHub Actions"""
    if "CI" in os.environ:
        type = type.lower()
        print(f"::{type}::{message}")
    else:
        type = type.upper()
        print(f"{type}: {message}")


def get_local_resources(tx_config):
    """Read resources in .tx/config and returns a list of resource slug"""
    config = configparser.ConfigParser()
    config.read(tx_config)

    if len(config.sections()) == 0:
        # incorrect file, empty list
        printmsg("error", f"'{tx_config}' is not a valid Transifex configuration file.")
        exit(1)

    if len(config.sections()) <= 1:
        # correct file, zero resources
        printmsg("error", f"'{tx_config}' not initialized yet.")
        exit(1)

    resources = []
    for section in config.sections():
        section = section.split(":r:", 1)

        # Eliminate the main configuration, and remote project identifier
        if section[0] == "main":
            continue
        else:
            resources.append(section[1])

    print("Successfully retrieved local resources!")

    return resources


def get_remote_resources(project):
    """Return a generator containing all the project's resources"""
    return transifex_api.Resource.filter(project=project).all()


def get_unused_resources(remote_resources, local_resources, dry_run):
    """Compare local an remote resources and returns a dict with the unused ones"""
    unused_resources = {}
    for resource in remote_resources:
        if resource.slug not in local_resources:
            if not resource.accept_translations:
                last_update = dateutil.parser.parse(resource.datetime_modified)
                current_time = datetime.now().replace(tzinfo=dateutil.tz.UTC)
                delete_status = (current_time - last_update).days >= 3
                if delete_status and not dry_run:
                    printmsg(
                        "warning",
                        f"Deleting '{resource.slug}', locked for 3 days or more.",
                    )
                    # resource.delete()
                elif delete_status and dry_run:
                    printmsg(
                        "warning",
                        f"'{resource.slug}' would be deleted now, but this is dry-run mode.",
                    )

                continue

            unused_resources[resource.slug] = resource

    return unused_resources


def lock_resources(unused_resources, dry_run):
    """Lock resources considered as unused, so they can be considered for deletion"""
    for resource in unused_resources.values():
        if not dry_run:
            printmsg("warning", f"Locking '{resource.slug}' ... ")
            # resource.attributes["accept_translations"] = False
            # resource.save("accept_translations")
        else:
            printmsg(
                "warning",
                f"'{resource.slug}' would be locked now, but this is dry-run mode.",
            )


def main():
    arg_parser = argparse.ArgumentParser(description=__doc__)
    arg_parser.add_argument(
        "tx_config_path",
        type=str,
        help="path to Transifex config file",
    )
    arg_parser.add_argument(
        "--dry-run",
        "-d",
        action="store_true",
        help="If set, print what would be done but no lock/delete is done",
    )
    args = vars(arg_parser.parse_args())

    tx_config_path = args["tx_config_path"]
    dry_run = args["dry_run"]
    organization_slug = os.getenv("SPHINXINTL_TRANSIFEX_ORGANIZATION_NAME")
    project_slug = os.getenv("SPHINXINTL_TRANSIFEX_PROJECT_NAME")

    print("Using TX Config Path:", tx_config_path)
    print("Using organization:", organization_slug)
    print("Using project:", project_slug)

    local_resources = get_local_resources(tx_config_path)

    transifex_api.setup(auth=os.getenv("TX_TOKEN"))
    ORGANIZATION = transifex_api.Organization.get(slug=organization_slug)
    PROJECT = ORGANIZATION.fetch("projects").get(slug=project_slug)
    remote_resources = get_remote_resources(PROJECT)

    unused_resources = get_unused_resources(remote_resources, local_resources, dry_run)

    if len(unused_resources) == 0:
        print("All resources are locked or in use!")
    else:
        lock_resources(unused_resources, dry_run)


if __name__ == "__main__":
    main()
