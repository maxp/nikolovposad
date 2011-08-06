#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join as path_join

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

HTML_DIR = os.path.join(os.path.dirname(__file__), 'html')

class MainHandler(webapp.RequestHandler):
    def get(self):

        self.response.out.write(
            template.render(
                path_join(HTML_DIR, 'mainpage.html'),
                {'var':'val'}
            )
        )


def main():
    application = webapp.WSGIApplication([('/', MainHandler)], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()

#.