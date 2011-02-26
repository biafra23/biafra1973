#!/usr/bin/env python
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import logging
import os

class MainHandler(webapp.RequestHandler):

    def post(self):
#        for name in os.environ.keys():
#            self.response.out.write("%s = %s<br />\n" % (name, os.environ[name]))

        logging.debug("chat.get()")
        logging.info("chat.get()")
        logging.error("chat.get()")

#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.out.write('')


def main():
    application = webapp.WSGIApplication([('/', MainHandler)], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
