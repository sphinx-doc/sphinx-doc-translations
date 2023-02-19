"""
We must keep old "pot" files in the "./pot/" directory to avoid commit
for only "POT-Creation-Time" line updated.
refs: https://github.com/sphinx-doc/sphinx/issues/3443

So we use the procedure as bellow:

1. update "./pot/" directory by "sphinx-build -b gettext"
2. remove unused pot file from "./pot" directory by this "autoremove.py" script
"""

import argparse
import os
import subprocess
import textwrap
from shutil import which

from pathlib import Path
from sphinx.application import Sphinx

TRANSIFEX_CLI_MINIMUM_VERSION = (1, 2, 1)

CMD_TMPL = (
    'tx',
    'delete',
    '--organization', '%(transifex_organization_name)s',
    '--project', '%(transifex_project_name)s',
    '--resource', '%(resource_name)s',
    '--file-filter', '%(locale_dir)s/<lang>/LC_MESSAGES/%(resource_path)s.po',
    '%(pot_dir)s/%(resource_path)s.pot',
)


def main():
    check_transifex_cli_installed()

    parser = argparse.ArgumentParser()
    parser.add_argument('sourcedir',
                        help=('path to documentation source files'))
    parser.add_argument('outputdir',
                        help=('path to output directory'))
    args = parser.parse_args()

    proj_slug = os.environ["SPHINXINTL_TRANSIFEX_PROJECT_NAME"]
    outdir = Path(args.outputdir)

    app = Sphinx(
        srcdir=args.sourcedir,
        confdir=args.sourcedir,
        outdir=outdir,
        doctreedir=(outdir / '.doctrees'),
        buildername='gettext'
    )
    new_pots = set((outdir / f"{d}.pot") for d in app.env.all_docs)
    if not new_pots:
        print("Generated pot files are not exist. ABORT.")
    else:
        old_pots = set(outdir.glob('**/*.pot'))
        to_be_removed = sorted(old_pots - new_pots)
        print("Remove unused pot files ... ")
        for p in to_be_removed:
            resource = str(p.relative_to(outdir).stem).replace("/", "--")
            res = f"{proj_slug}.{resource}"
            cmd_args = ["tx", "delete", res]
            print("RUN:", " ".join(cmd_args))
            ret = subprocess.run(cmd_args, encoding="utf-8", capture_output=True)
            print(ret.stdout)
            if ret.returncode:
                breakpoint()
                raise RuntimeError(ret.stderr)
            # p.unlink()
            print("Removed: ", res)


# copy from https://github.com/sphinx-doc/sphinx-intl/blob/c327016e/sphinx_intl/transifex.py#L59
def check_transifex_cli_installed():
    tx_cli_url = 'https://raw.githubusercontent.com/transifex/cli/master/install.sh'
    if not which("tx"):
        msg = textwrap.dedent(f"""\
            Could not run "tx".
            You need to install the Transifex CLI external library.
            Please install the below command and restart your terminal \
            if you want to use this action:

                $ curl -o- {tx_cli_url} | bash

            """)
        raise RuntimeError(msg)

    version_msg = subprocess.check_output("tx --version", shell=True, encoding="utf-8")

    if not version_msg.startswith("TX Client"):
        msg = textwrap.dedent(f"""\
            The old transifex_client library was found.
            You need to install the Transifex CLI external library.
            Please install the below command and restart your terminal \
            if you want to use this action:

                $ curl -o- {tx_cli_url} | bash

            """)
        raise RuntimeError(msg)

    version = tuple(int(x) for x in version_msg.split("=")[-1].strip().split("."))

    if not version >= TRANSIFEX_CLI_MINIMUM_VERSION:
        msg = textwrap.dedent(f"""\
        An unsupported version of the Transifex CLI was found.
        Version {TRANSIFEX_CLI_MINIMUM_VERSION} or greater is required.
        Please run the below command if you want to use this action:

            $ tx update

        """)
        raise RuntimeError(msg)


if __name__ == '__main__':
    main()
