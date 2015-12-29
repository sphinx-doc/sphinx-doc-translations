import os
parent = os.path.dirname
BASEDIR = parent(parent(parent(os.path.abspath(__file__))))

execfile(os.path.join(BASEDIR, 'sphinx/doc/conf.py'))

language = 'ja'

locale_dirs = [os.path.join(BASEDIR, 'locale/')]

def setup(app):
    app.srcdir = os.path.join(BASEDIR, 'sphinx/doc/')
    app.confdir = app.srcdir

