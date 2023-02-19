#!/bin/sh

set -ex

# setup environment
SPHINXINTL_TRANSIFEX_ORGANIZATION_NAME=sphinx-doc
SPHINXINTL_TRANSIFEX_USERNAME=sphinxjp
SPHINXINTL_TRANSIFEX_TOKEN=token
SPHINXINTL_TRANSIFEX_PROJECT_NAME=sphinx-doc
find sphinx -name "*.pyc" -exec rm {} \;
git checkout master
git submodule init
git submodule update
(cd sphinx; git fetch origin; git checkout -b master origin/master)
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
