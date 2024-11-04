#!/bin/sh
# update transifex pot and local po files

set -ex

LANGS='ar ca_ES de es fr it_IT ja ko pl_PL pt_BR ru sr zh_CN'

LANGS_PULL=$(echo $LANGS | sed 's| |,|g')

# pull po files from transifex
cd `dirname $0`

# Skip Transifex commands when running pull requests event on GitHub Actions
if [ -n "$GITHUB_EVENT_NAME" ] && [ "$GITHUB_EVENT_NAME" != 'pull_request' ]; then
  tx push -s --skip
  rm -R -f ${LANGS}
  tx pull --silent -f -l ${LANGS_PULL}
fi

git checkout .tx/config
