# Sphinx official documentation translations

This is a project to provide Sphinx official documentation, hosted on the Read The Docs platform, in multiple languages.

> **Note:** The current procedure is bit tricky because Read The Docs doesn't have a way to specify options for `sphinx-build` command.
**conf.py** files for each languages have `language` and `locale_dirs` values without having full copy of **conf.py** of sphinx doc. If we want to specify **conf.py** file that is out of source directory, we will use `-c` option for the `sphinx-build` command. Unfortunately Read the Docs doesn't support that. If there is a better way, open an issue.

## URLs

* RTD project pages for Sphinx:

  * [![Documentation Status](https://readthedocs.org/projects/sphinx/badge/?version=master)](https://www.sphinx-doc.org/en/master/?badge=master) https://readthedocs.org/projects/sphinx/  (Parent project)
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-ar/badge/?version=master)](https://www.sphinx-doc.org/ar/master/?badge=master) https://readthedocs.org/projects/sphinx-ar/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-ca-es/badge/?version=master)](https://www.sphinx-doc.org/ca/master/?badge=master) https://readthedocs.org/projects/sphinx-ca-es/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-zh-cn/badge/?version=master)](https://www.sphinx-doc.org/zh_CN/master/?badge=master) https://readthedocs.org/projects/sphinx-zh-cn/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-fr/badge/?version=master)](https://www.sphinx-doc.org/fr/master/?badge=master)
https://readthedocs.org/projects/sphinx-fr/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-de/badge/?version=master)](https://www.sphinx-doc.org/de/master/?badge=master)
https://readthedocs.org/projects/sphinx-de/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-it-it/badge/?version=master)](https://www.sphinx-doc.org/it/master/?badge=master)
https://readthedocs.org/projects/sphinx-it-it/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-ja/badge/?version=master)](https://www.sphinx-doc.org/ja/master/?badge=master)
 https://readthedocs.org/projects/sphinx-ja/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-ko/badge/?version=master)](https://www.sphinx-doc.org/ko/master/?badge=master)
https://readthedocs.org/projects/sphinx-ko/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-pl-pl/badge/?version=master)](https://www.sphinx-doc.org/pl/master/?badge=master)
https://readthedocs.org/projects/sphinx-pl-pl/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-pt-br/badge/?version=master)](https://www.sphinx-doc.org/pt_BR/master/?badge=master)
https://readthedocs.org/projects/sphinx-pt-br/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-doc-ru/badge/?version=master)](https://www.sphinx-doc.org/ru/master/?badge=master)
https://readthedocs.org/projects/sphinx-doc-ru/ (Other project "sphinx-ru" is already exist.)
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-sr/badge/?version=master)](https://www.sphinx-doc.org/sr/master/?badge=master)
https://readthedocs.org/projects/sphinx-sr/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-sr-rs/badge/?version=latest)](https://sphinx-sr-rs.readthedocs.io/sr/latest/?badge=latest)
https://readthedocs.org/projects/sphinx-sr-rs/
  * [![Documentation Status](https://readthedocs.org/projects/sphinx-es/badge/?version=master)](https://www.sphinx-doc.org/es/master/?badge=master)
https://readthedocs.org/projects/sphinx-es/

* Documentation pages for each languages:

  * http://www.sphinx-doc.org/en
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

Instructions: https://docs.readthedocs.org/en/latest/localization.html#project-with-multiple-translations

Key points:

* There must be a RTD project for each language.
* Each projects must have correct Language setting on "Settings" page.
* Parent project must have connections to each translated project on the "Translations Settings" page.

## How to add a new language

1. Add new language to `locale/update.sh`:

   ```diff
   - rm -R es ja
   - tx pull -l es,ja
   + rm -R es ja pt_BR
   + tx pull -l es,ja,pt_BR
   ```

2. Update po files:

   ```
   sh ./locale/update.sh
   ```

4. Commit them

5. Add new project on Read The Docs:

   https://readthedocs.org/projects/sphinx-pt-br/

6. Add new translation project to parent project:

   https://readthedocs.org/dashboard/sphinx/translations/

