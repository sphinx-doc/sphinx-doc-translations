#!/bin/sh
# update transifex pot and local po files

set -ex

# required environment variables
# SPHINXINTL_TRANSIFEX_ORGANIZATION_NAME=sphinx-doc
# SPHINXINTL_TRANSIFEX_PROJECT_NAME=sphinx-doc
# SPHINXINTL_TRANSIFEX_USERNAME=sphinxjp
# SPHINXINTL_TRANSIFEX_TOKEN=...


# pull po files from transifex
cd `dirname $0`
sphinx-intl create-transifexrc
sphinx-build -T -b gettext ../sphinx/doc pot
sphinx-intl update-txconfig-resources -p pot -d .
python autoremove.py ../sphinx/doc pot
cat .tx/config
tx push -s --skip
rm -R -f ar ca_ES zh_CN fr de it_IT ja ko pl_PL pt_BR ru sr sr_RS es
tx pull -l ar,ca_ES,zh_CN,fr,de,it_IT,ja,ko,pl_PL,pt_BR,ru,sr,sr_RS,es
git checkout .tx/config

