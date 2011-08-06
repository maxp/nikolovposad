#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(
            """
<!DOCTYPE html>
<html><head><title>Nikolov Posad village, Irkutsk, Russia</title>
</head>
<body style="font: normal 14px Verdana, sans-serif;">
<div style="text-align: center; margin: 3em 10em;">

<h1>Поселок Николов Посад</h1>
<br/>Иркутский район

<a href="http://maps.google.com/?ll=52.229823,104.245234&spn=0.014247,0.049739&t=h&z=15"><br/>
<br/>
<iframe width="600" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
  src="http://maps.google.com/?ie=UTF8&amp;hq=&amp;hnear=Irkutsk,+Irkutsk+Oblast,+Russia&amp;ll=52.229823,104.245234&amp;spn=0.014247,0.049739&amp;t=h&amp;z=15&amp;output=embed&amp;hl=ru"></iframe>
</div>
</body>
</html>
            """
        )


def main():
    application = webapp.WSGIApplication([('/', MainHandler)], debug=True)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()

#.