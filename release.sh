#!/bin/sh

set -e

if [ -z "$1" ]; then
    echo "$0 [version]"
    exit 1
fi

RELEASE=$1
BRANCH=`echo $RELEASE | cut -d . -f 1,2`

git submodule init
git submodule update
(cd sphinx; git fetch origin)
find sphinx -name "*.pyc" -exec rm {} \;

# update x.y branch
git co $BRANCH
cd sphinx
git co $RELEASE
cd ../locale
pip install -r requirements.txt
sphinx-intl create-transifexrc
sh update.sh
cd ..
git add locale sphinx
git commit -am "use sphinx-$RELEASE"

# update stable branch
git co stable
cd sphinx
git co $RELEASE
cd ../locale
pip install -r requirements.txt
sphinx-intl create-transifexrc
sh update.sh
cd ..
git add locale sphinx
git commit -am "use sphinx-$RELEASE"

# push changes
git co master
git submodule update
git push origin stable $BRANCH
