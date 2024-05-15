#!/bin/sh
# Update POT files and Transifex configuration file

set -ex

# required environment variables
# SPHINXINTL_TRANSIFEX_ORGANIZATION_NAME=sphinx-doc
# SPHINXINTL_TRANSIFEX_PROJECT_NAME=sphinx-doc
# TX_TOKEN=...

cd `dirname $0`
#rm -R pot  # skip this line cause "already unused pot files will not removed" but we must keep these files to avoid commit for only "POT-Creation-Time" line updated. see: https://github.com/sphinx-doc/sphinx/issues/3443
sphinx-build -T -j auto -b gettext ../sphinx/doc pot
sphinx-intl update-txconfig-resources -p pot -d .
