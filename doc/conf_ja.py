import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

execfile(os.path.join(BASEDIR, 'sphinx/doc/conf.py'))

language = 'ja'

locale_dirs = [os.path.join(BASEDIR, 'locale/')]

def setup(app):
    app.srcdir = os.path.join(BASEDIR, 'sphinx/doc/')
    app.confdir = app.srcdir

