Sphinx official documentation translations
==========================================

This is a project to provide Sphinx official documentation, hosted on the Read The Docs platform, in multiple languages.

.. note:: The current procedure is bit tricky because Read The Docs doesn't have a way to specify options for ``sphinx-build`` command.
   **conf.py** files for each languages have ``language`` and ``locale_dirs`` values without having full copy of **conf.py** of sphinx doc.
   If we want to specify **conf.py** file that is out of source directory, we will use ``-c`` option for the ``sphinx-build`` command.
   Unfortunately Read the Docs doesn't support that. If there is a better way, open an issue.

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
     - http://www.sphinx-doc.org/zh_CN
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
     - http://www.sphinx-doc.org/pt_BR
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

      - rm -R es ja
      - tx pull -l es,ja
      + rm -R es ja pt_BR
      + tx pull -l es,ja,pt_BR

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

