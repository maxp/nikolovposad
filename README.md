
Nikolov Posad village
=====================

Google Appengine website


.

.

.

.

.



VirtualEnv Appengine fixes
--------------------------



    virtualenv --no-site-packages gae
    cd gae
    bin/activate
    easy_install PIL

    /opt/google_appengine/google/appengine/tools/dev_appserver.py:

    ALLOWED_DIRS = set([
        os.path.normcase(os.path.realpath(os.path.dirname(os.__file__))),
        os.path.normcase(os.path.abspath(os.path.dirname(os.__file__))),
        os.path.normcase(os.path.dirname(os.path.realpath(os.__file__))),
        os.path.normcase(os.path.dirname(os.path.abspath(os.__file__))),

        ### virtualenv fix
        os.path.normcase(os.path.realpath(os.path.dirname(cgi.__file__))),
        os.path.normcase(os.path.abspath(os.path.dirname(cgi.__file__))),
        os.path.normcase(os.path.dirname(os.path.realpath(cgi.__file__))),
        os.path.normcase(os.path.dirname(os.path.abspath(cgi.__file__))),
        ###
    ])


    ~virtualenv/lib/python2.6/site-packages/gae.pth:
    /opt/google_appengine

    cd ~virtualenv/bin
    ln -s /opt/google_appengine/appcgf.py .
    ln -s /opt/google_appengine/dev_appserver.py .

.