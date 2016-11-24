export SPHINXINTL_TRANSIFEX_PROJECT_NAME=sphinx-doc-1_4

cd `dirname $0`
rm -Rf pot
sphinx-build -b gettext ../sphinx/doc pot
sphinx-intl update-txconfig-resources -p pot -d .
rm -Rf es ja pt_BR
tx pull -l es,ja,pt_BR
git checkout .tx/config

