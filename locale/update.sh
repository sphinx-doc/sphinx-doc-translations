#!/bin/sh
# update transifex pot and local po files

set -ex

# required environment variables
# SPHINXINTL_TRANSIFEX_USERNAME=sphinxjp
# SPHINXINTL_TRANSIFEX_PROJECT_NAME=sphinx-doc


# pull po files from transifex
cd `dirname $0`
/home/runner/.local/bin/sphinx-intl create-transifexrc
#rm -R pot  # skip this line cause "already unused pot files will not removed" but we must keep these files to avoid commit for only "POT-Creation-Time" line updated. see: https://github.com/sphinx-doc/sphinx/issues/3443
/home/runner/.local/bin/sphinx-build -T -b gettext ../sphinx/doc pot
/home/runner/.local/bin/sphinx-intl update-txconfig-resources -p pot -d .
cat .tx/config
/home/runner/.local/bin/tx push -s --skip
rm -R -f ar ca_ES zh_CN fr de it_IT ja ko pl_PL pt_BR ru sr sr_RS es
tx pull -l ar,ca_ES,zh_CN,fr,de,it_IT,ja,ko,pl_PL,pt_BR,ru,sr,sr_RS,es
git checkout .tx/config

