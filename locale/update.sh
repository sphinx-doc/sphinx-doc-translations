#!/bin/sh
# update transifex pot and local po files

set -ex

# required environment variables
# SPHINXINTL_TRANSIFEX_USERNAME=sphinxjp
# SPHINXINTL_TRANSIFEX_PROJECT_NAME=sphinx-doc-1_7


# pull po files from transifex
cd `dirname $0`
sphinx-intl create-transifexrc
#rm -R pot  # skip this line cause "already unused pot files will not removed" but we must keep these files to avoid commit for only "POT-Creation-Time" line updated. see: https://github.com/sphinx-doc/sphinx/issues/3443
sphinx-build -T -b gettext ../sphinx/doc pot
sphinx-intl update-txconfig-resources -p pot -d .
cat .tx/config
tx push -s --skip
rm -R es ja pt_BR
tx pull -l es,ja,pt_BR
git checkout .tx/config

