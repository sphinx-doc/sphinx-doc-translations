#!/usr/bin/env python3
"""
Locks obsolete resources in a Transifex project,
then remove them after 3 days remove them if still locked.

The following variables need to be set:
- SPHINXINTL_TRANSIFEX_ORGANIZATION_NAME
- SPHINXINTL_TRANSIFEX_PROJECT_NAME
- TX_TOKEN
"""

import os
import argparse
import configparser
import dateutil.parser
import dateutil.tz
from datetime import datetime

import requests

API_BASE_URL = "https://rest.api.transifex.com"


def printmsg(type, message):
    """Format message in case it is being run in GitHub Actions"""
    if "CI" in os.environ:
        type = type.lower()
        print(f"::{type}::{message}")
    else:
        type = type.upper()
        print(f"{type}: {message}")


def get_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/vnd.api+json",
    }


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
        section_parts = section.split(":r:", 1)

        if section_parts[0] == "main":
            continue
        else:
            resources.append(section_parts[1])

    print("Successfully retrieved local resources!")
    return resources


def get_remote_resources(headers, organization_slug, project_slug):
    """Fetch all resources from the specified organization and project, handling pagination."""
    project_id = f"o:{organization_slug}:p:{project_slug}"
    url = f"{API_BASE_URL}/resources"
    params = {"filter[project]": project_id}
    resources = []

    while url:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        resources.extend(data.get("data", []))

        # Handles pagination (if there is more than one resource page)
        url = data.get("links", {}).get("next")
        params = None

    return resources


def delete_resource(headers, resource_id):
    """Deletes a resource via Transifex API v3."""
    url = f"{API_BASE_URL}/resources/{resource_id}"
    response = requests.delete(url, headers=headers)
    response.raise_for_status()


def patch_resource_lock(headers, resource_id, accept_translations=False):
    """Updates the accept_translations attribute of a resource."""
    url = f"{API_BASE_URL}/resources/{resource_id}"
    payload = {
        "data": {
            "id": resource_id,
            "type": "resources",
            "attributes": {
                "accept_translations": accept_translations
            }
        }
    }
    response = requests.patch(url, headers=headers, json=payload)
    response.raise_for_status()


def get_unused_resources(remote_resources, local_resources, headers, dry_run):
    """Compare local and remote resources and returns a dict with the unused ones"""
    unused_resources = {}

    for resource in remote_resources:
        attributes = resource.get("attributes", {})
        slug = attributes.get("slug")
        accept_translations = attributes.get("accept_translations", True)
        datetime_modified = attributes.get("datetime_modified")
        resource_id = resource.get("id")

        if slug not in local_resources:
            if not accept_translations:
                last_update = dateutil.parser.parse(datetime_modified)
                current_time = datetime.now(tz=dateutil.tz.UTC)
                delete_status = (current_time - last_update).days >= 3

                if delete_status and not dry_run:
                    printmsg(
                        "warning",
                        f"Deleting '{slug}', locked for 3 days or more.",
                    )
                    delete_resource(headers, resource_id)
                elif delete_status and dry_run:
                    printmsg(
                        "warning",
                        f"'{slug}' would be deleted now, but this is dry-run mode.",
                    )

                continue

            unused_resources[slug] = resource

    return unused_resources


def lock_resources(unused_resources, headers, dry_run):
    """Lock resources considered as unused, so they can be considered for deletion"""
    for slug, resource in unused_resources.items():
        resource_id = resource.get("id")
        if not dry_run:
            printmsg("warning", f"Locking '{slug}' ... ")
            patch_resource_lock(headers, resource_id, accept_translations=False)
        else:
            printmsg(
                "warning",
                f"'{slug}' would be locked now, but this is dry-run mode.",
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
    tx_token = os.getenv("TX_TOKEN")

    if not tx_token:
        printmsg("error", "TX_TOKEN environment variable is not set.")
        exit(1)

    print("Using TX Config Path:", tx_config_path)
    print("Using organization:", organization_slug)
    print("Using project:", project_slug)

    local_resources = get_local_resources(tx_config_path)
    headers = get_headers(tx_token)

    remote_resources = get_remote_resources(headers, organization_slug, project_slug)
    unused_resources = get_unused_resources(remote_resources, local_resources, headers, dry_run)

    if len(unused_resources) == 0:
        print("All resources are locked or in use!")
    else:
        lock_resources(unused_resources, headers, dry_run)


if __name__ == "__main__":
    main()
