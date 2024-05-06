#!/bin/sh
# update transifex pot and local po files

set -ex

# required environment variables
# SPHINXINTL_TRANSIFEX_ORGANIZATION_NAME=sphinx-doc
# SPHINXINTL_TRANSIFEX_PROJECT_NAME=sphinx-doc
# TX_TOKEN=...

# pull po files from transifex
cd `dirname $0`
#rm -R pot  # skip this line cause "already unused pot files will not removed" but we must keep these files to avoid commit for only "POT-Creation-Time" line updated. see: https://github.com/sphinx-doc/sphinx/issues/3443
sphinx-build -T -b gettext ../sphinx/doc pot
sphinx-intl update-txconfig-resources -p pot -d .
cat .tx/config

# Skip Transifex commands when running pull requests event on GitHub Actions
if [[ -z "$CI" || "$GITHUB_EVENT_NAME" != 'pull_request' ]]; then
  tx push -s --skip
  rm -R -f ar ca_ES zh_CN fr de it_IT ja ko pl_PL pt_BR ru sr es
  tx pull --silent -f -l ar,ca_ES,zh_CN,fr,de,it_IT,ja,ko,pl_PL,pt_BR,ru,sr,es
fi

git checkout .tx/config

