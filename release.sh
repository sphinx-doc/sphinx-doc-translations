#!/bin/sh

set -ex

RELEASE=1_7

# setup environment
SPHINXINTL_TRANSIFEX_USERNAME=sphinxjp
SPHINXINTL_TRANSIFEX_PROJECT_NAME=sphinx-doc-${RELEASE}
find sphinx -name "*.pyc" -exec rm {} \;
git checkout master
git submodule init
git submodule update
# checkout sphinx master
(cd sphinx; git fetch origin; git checkout master)
pip install -r requirements.txt


# update transifex pot and local po files
sh ./locale/update.sh

# commit po(t) files
git add locale sphinx
git commit -m "[skip ci] update po(t) files"

# push changes
git checkout master
git submodule update
git push origin master
