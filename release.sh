#!/bin/sh

set -ex

RELEASE=1_6

# setup environment
SPHINXINTL_TRANSIFEX_USERNAME=sphinxjp
SPHINXINTL_TRANSIFEX_PROJECT_NAME=sphinx-doc-${RELEASE}
find sphinx -name "*.pyc" -exec rm {} \;
git checkout 1.6
git submodule init
git submodule update
(cd sphinx; git fetch origin; git checkout 1.6)
pip install -r requirements.txt


# update transifex pot and local po files
sh ./locale/update.sh

# commit po(t) files
git add locale sphinx
git commit -m "[skip ci] update po(t) files"

# push changes
git checkout 1.6
git submodule update
git push origin 1.6
