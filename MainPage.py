import webapp2
import random
import datetime
import jinja2
import os
from google.appengine.ext import ndb
import Event


jinja_env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
)
class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        main_template= jinja_env.get_template('MP.html')
        html= main_template.render()
        self.response.write(html)


app= webapp2.WSGIApplication([
    ('/', MainPageHandler)
],debug=True)
