# BASEDIR is set by <lang>/conf.py

execfile(os.path.join(BASEDIR, 'sphinx/doc/conf.py'))

locale_dirs = [os.path.join(BASEDIR, 'locale/')]

def setup(app):
    app.srcdir = os.path.join(BASEDIR, 'sphinx/doc/')
    app.confdir = app.srcdir

