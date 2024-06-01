#!/bin/sh
# setup

set -ex

sudo apt-get update && sudo apt-get install -y graphviz
pip install -U pip setuptools
pip install -r requirements.txt

# Install Transifex CLI tool into /usr/local/bin
# refer to Installation instructions https://github.com/transifex/cli#installation

(cd /usr/local/bin && curl -o- https://raw.githubusercontent.com/transifex/cli/master/install.sh | sudo bash)
