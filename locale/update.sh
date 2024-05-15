#!/bin/sh
# update transifex pot and local po files

set -ex

LANGS='ar ca_ES de es fr it_IT ja ko pl_PL pt_BR ru sr zh_CN'

LANGS_PULL=$(echo $LANGS | sed 's| |,|g')

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
if [[ "$GITHUB_EVENT_NAME" != 'pull_request' ]]; then
  tx push -s --skip
  rm -R -f ${LANGS}
  tx pull --silent -f -l ${LANGS_PULL}
fi

