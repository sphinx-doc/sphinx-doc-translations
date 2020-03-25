# sphinx-doc.org on the Read The Docs.
[![Build Status](https://travis-ci.org/sphinx-doc/sphinx-doc-translations.svg?branch=master)](https://travis-ci.org/sphinx-doc/sphinx-doc-translations)
[![Documentation Status](https://readthedocs.org/projects/sphinx/badge/?version=master)](https://www.sphinx-doc.org/en/master/?badge=master)

This is a project to provide Sphinx official documentation with multiple versions and multiple languages on Read The Docs site.

Current procedure is bit tricky because Read The Docs doesn't have a way to specify options for sphinx-build command.
conf.py files for each languages have 'language' and 'locale_dirs' values without having full copy of conf.py of sphinx doc. If we want to specify conf.py file that is out of source directory, we will use '-c' option for sphinx-build command. Unfortunately Read the Docs can't. If there are any better way, please let me know.

## URLs

* RTD project pages for Sphinx:

  * https://readthedocs.org/projects/sphinx/  (Master)
  * https://readthedocs.org/projects/sphinx-ar/
  * https://readthedocs.org/projects/sphinx-ca-es/
  * https://readthedocs.org/projects/sphinx-zh-cn/
  * https://readthedocs.org/projects/sphinx-fr/
  * https://readthedocs.org/projects/sphinx-de/
  * https://readthedocs.org/projects/sphinx-it-it/
  * https://readthedocs.org/projects/sphinx-ja/
  * https://readthedocs.org/projects/sphinx-ko/
  * https://readthedocs.org/projects/sphinx-pl-pl/
  * https://readthedocs.org/projects/sphinx-pt-br/
  * https://readthedocs.org/projects/sphinx-doc-ru/ (Other project "sphinx-ru" is already exist.)
  * https://readthedocs.org/projects/sphinx-sr/
  * https://readthedocs.org/projects/sphinx-sr-rs/
  * https://readthedocs.org/projects/sphinx-es/

* Documentation pages for each languages:

  * http://www.sphinx-doc.org/
  * http://www.sphinx-doc.org/ar
  * http://www.sphinx-doc.org/ca_ES
  * http://www.sphinx-doc.org/zh_CN
  * http://www.sphinx-doc.org/fr
  * http://www.sphinx-doc.org/de
  * http://www.sphinx-doc.org/it_IT
  * http://www.sphinx-doc.org/ja
  * http://www.sphinx-doc.org/ko
  * http://www.sphinx-doc.org/pl_PL
  * http://www.sphinx-doc.org/pt_BR
  * http://www.sphinx-doc.org/ru (Other project "sphinx-ru" is already exist.)
  * http://www.sphinx-doc.org/sr
  * http://www.sphinx-doc.org/sr_RS
  * http://www.sphinx-doc.org/es

## How to setup a translated documentation project on RTD

Detail is here: https://docs.readthedocs.org/en/latest/localization.html#project-with-multiple-translations

Points are:

* We must have RTD projects for each languages.
* Each projects must have correct Language setting on "Settings" page.
* Master project has connections to each translated projects on "translations settings" page.


## How to update po files

```
sh ./locale/update.sh
```

After that, you should commit updated po files.


## How to add a language

1. add language to locale/update.sh:

   ```
   - rm -R es ja
   - tx pull -l es,ja
   + rm -R es ja pt_BR
   + tx pull -l es,ja,pt_BR
   ```

2. update po files

3. commit them

4. add new project on Read The Docs like:

   https://readthedocs.org/projects/sphinx-pt-br/

5. add translation project to parent project like:

   https://readthedocs.org/dashboard/sphinx/translations/


## How to add a new version

1. add tag `1.7`

   ```
   git tag 1.7
   ```

2. replace old version `1_7` with `1_8` in:

   - release.sh
   - .travis.yml

3. commit it and push them:

   ```
   git add release.sh .travis.yml
   git commit -m "add new version: 1.8"
   git push --tags
   ```

4. enable version 1.7 on RTD:

   https://readthedocs.org/projects/sphinx-ja/versions/

