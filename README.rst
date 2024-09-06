Sphinx official documentation translations
==========================================

|main| |test|

.. |main| image:: https://github.com/sphinx-doc/sphinx-doc-translations/actions/workflows/main.yml/badge.svg
          :target: https://github.com/sphinx-doc/sphinx-doc-translations/actions/workflows/main.yml
          :alt: Badge for the update status

.. |test| image:: https://github.com/sphinx-doc/sphinx-doc-translations/actions/workflows/test-translations.yml/badge.svg
          :target: https://github.com/sphinx-doc/sphinx-doc-translations/actions/workflows/test-translations.yml
          :alt: Badge for the translation tests

This is a project to provide Sphinx official documentation, hosted on the Read The Docs platform, in multiple languages.

How the translated documentation projects are setup on RTD
----------------------------------------------------------

Instructions: https://docs.readthedocs.org/en/latest/localization.html#project-with-multiple-translations

Key points:

* There is a RTD project for each language.
* Each project needs the correct **Language** setting on the **Settings** page.
* The parent project needs connections created to each translated project on the **Translations Settings** page.

.. list-table::
   :header-rows: 1

   * - Build Status
     - sphinx-doc docs
     - RTD Project
   * - .. image:: https://readthedocs.org/projects/sphinx/badge/?version=master
          :target: https://www.sphinx-doc.org/en/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/en
     - https://readthedocs.org/projects/sphinx/ (Parent project)
   * - .. image:: https://readthedocs.org/projects/sphinx-ar/badge/?version=master
          :target: https://www.sphinx-doc.org/ar/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/ar
     - https://readthedocs.org/projects/sphinx-ar/
   * - .. image:: https://readthedocs.org/projects/sphinx-ca-es/badge/?version=master
          :target: https://www.sphinx-doc.org/ca/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/ca
     - https://readthedocs.org/projects/sphinx-ca-es/
   * - .. image:: https://readthedocs.org/projects/sphinx-zh-cn/badge/?version=master
          :target: https://www.sphinx-doc.org/zh_CN/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/zh-cn
     - https://readthedocs.org/projects/sphinx-zh-cn/
   * - .. image:: https://readthedocs.org/projects/sphinx-fr/badge/?version=master
          :target: https://www.sphinx-doc.org/fr/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/fr
     - https://readthedocs.org/projects/sphinx-fr/
   * - .. image:: https://readthedocs.org/projects/sphinx-de/badge/?version=master
          :target: https://www.sphinx-doc.org/de/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/de
     - https://readthedocs.org/projects/sphinx-de/
   * - .. image:: https://readthedocs.org/projects/sphinx-it-it/badge/?version=master
          :target: https://www.sphinx-doc.org/it/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/it
     - https://readthedocs.org/projects/sphinx-it-it/
   * - .. image:: https://readthedocs.org/projects/sphinx-ja/badge/?version=master
          :target: https://www.sphinx-doc.org/ja/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/ja
     - https://readthedocs.org/projects/sphinx-ja/
   * - .. image:: https://readthedocs.org/projects/sphinx-ko/badge/?version=master
          :target: https://www.sphinx-doc.org/ko/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/ko
     - https://readthedocs.org/projects/sphinx-ko/
   * - .. image:: https://readthedocs.org/projects/sphinx-pl-pl/badge/?version=master
          :target: https://www.sphinx-doc.org/pl/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/pl
     - https://readthedocs.org/projects/sphinx-pl-pl/
   * - .. image:: https://readthedocs.org/projects/sphinx-pt-br/badge/?version=master
          :target: https://www.sphinx-doc.org/pt_BR/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/pt-br
     - https://readthedocs.org/projects/sphinx-pt-br/
   * - .. image:: https://readthedocs.org/projects/sphinx-doc-ru/badge/?version=master
          :target: https://www.sphinx-doc.org/ru/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/ru
     - https://readthedocs.org/projects/sphinx-doc-ru/
   * - .. image:: https://readthedocs.org/projects/sphinx-sr/badge/?version=master
          :target: https://www.sphinx-doc.org/sr/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/sr
     - https://readthedocs.org/projects/sphinx-sr/
   * - .. image:: https://readthedocs.org/projects/sphinx-es/badge/?version=master
          :target: https://www.sphinx-doc.org/es/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/es
     - https://readthedocs.org/projects/sphinx-es/

How to add a new language translation
-------------------------------------

1. Add new language to ``locale/update.sh``:

   .. code-block:: diff

      - LANGS='es ja'
      + LANGS='es ja pt_BR'

2. Update po files:

   .. code-block::
                           
      sh ./locale/update.sh

4. Commit them

5. Add new project on Read The Docs. For example, for ``pt_BR``:

   https://readthedocs.org/projects/sphinx-pt-br/

   .. note:: If a RTD project name for a translation is already taken, create a unique project name instead.
      For example, when ``sphinx-ru`` was taken, ``sphinx-doc-ru`` was used instead.

7. Add new translation project to parent project:

   https://readthedocs.org/dashboard/sphinx/translations/

