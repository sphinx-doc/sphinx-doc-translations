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
   * - .. image:: https://app.readthedocs.org/projects/sphinx/badge/?version=master
          :target: https://www.sphinx-doc.org/en/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/en
     - https://app.readthedocs.org/projects/sphinx/ (Parent project)
   * - .. image:: https://app.readthedocs.org/projects/sphinx-ar/badge/?version=master
          :target: https://www.sphinx-doc.org/ar/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/ar
     - https://app.readthedocs.org/projects/sphinx-ar/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-ca-es/badge/?version=master
          :target: https://www.sphinx-doc.org/ca/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/ca
     - https://app.readthedocs.org/projects/sphinx-ca-es/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-de/badge/?version=master
          :target: https://www.sphinx-doc.org/de/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/de
     - https://app.readthedocs.org/projects/sphinx-de/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-es/badge/?version=master
          :target: https://www.sphinx-doc.org/es/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/es
     - https://app.readthedocs.org/projects/sphinx-es/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-fr/badge/?version=master
          :target: https://www.sphinx-doc.org/fr/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/fr
     - https://app.readthedocs.org/projects/sphinx-fr/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-it-it/badge/?version=master
          :target: https://www.sphinx-doc.org/it/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/it
     - https://app.readthedocs.org/projects/sphinx-it-it/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-ja/badge/?version=master
          :target: https://www.sphinx-doc.org/ja/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/ja
     - https://app.readthedocs.org/projects/sphinx-ja/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-ko/badge/?version=master
          :target: https://www.sphinx-doc.org/ko/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/ko
     - https://app.readthedocs.org/projects/sphinx-ko/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-pl-pl/badge/?version=master
          :target: https://www.sphinx-doc.org/pl/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/pl
     - https://app.readthedocs.org/projects/sphinx-pl-pl/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-pt-br/badge/?version=master
          :target: https://www.sphinx-doc.org/pt_BR/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/pt-br
     - https://app.readthedocs.org/projects/sphinx-pt-br/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-doc-ru/badge/?version=master
          :target: https://www.sphinx-doc.org/ru/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/ru
     - https://app.readthedocs.org/projects/sphinx-doc-ru/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-sr/badge/?version=master
          :target: https://www.sphinx-doc.org/sr/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/sr
     - https://app.readthedocs.org/projects/sphinx-sr/
   * - .. image:: https://app.readthedocs.org/projects/sphinx-zh-cn/badge/?version=master
          :target: https://www.sphinx-doc.org/zh_CN/master/?badge=master
          :alt: Documentation Status
     - http://www.sphinx-doc.org/zh-cn
     - https://app.readthedocs.org/projects/sphinx-zh-cn/

How to add a new language translation
-------------------------------------

1. Add new language to ``locales/update.sh``:

   .. code-block:: diff

      - LANGS='es ja'
      + LANGS='es ja pt_BR'

2. Update po files:

   .. code-block::

      sh ./locales/update.sh

4. Commit them

5. Add new project on Read The Docs. For example, for ``pt_BR``:

   https://app.readthedocs.org/projects/sphinx-pt-br/

   .. note:: If a RTD project name for a translation is already taken, create a unique project name instead.
      For example, when ``sphinx-ru`` was taken, ``sphinx-doc-ru`` was used instead.

7. Add new translation project to parent project:

   https://app.readthedocs.org/dashboard/sphinx/translations/

