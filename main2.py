#!/usr/bin/env python
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import logging
import os

class MainHandler(webapp.RequestHandler):
    
    def get(self):
        logging.debug("Foo logging Bar")
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("Version: %s\n" % os.environ["CURRENT_VERSION_ID"] )
#        for name in os.environ.keys():
#            self.response.out.write("%s = %s\n" % (name, os.environ[name]))


def main():
    application = webapp.WSGIApplication([('/', MainHandler)], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
