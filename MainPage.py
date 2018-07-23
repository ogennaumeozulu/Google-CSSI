import webapp2
import random
import datetime
import jinja2
import os
from google.appengine.ext import ndb
import Event
from FindEvents import FindEventsHandler

from SearchResults import SearchResultsHandler

from SearchResults import SearchResultsHandler
from CreateEvent import CreateEventHandler
#from login import LoginHandler

from google.appengine.ext import ndb
import Event

from FindEvents import FindEventsHandler
from login import LoginHandler
from CreateEvent import CreateEventHandler




jinja_env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
)
class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template('MP.html')
        html = main_template.render()
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/find', FindEventsHandler),
    ('/results', SearchResultsHandler),
<<<<<<< HEAD
    ('/create', CreateEventHandler),
    #('/login', LoginHandler)
=======
    ('/create', CreateEventHandler)
    # ('/login', LoginHandler)
>>>>>>> 827e90dc69a9d6df97be4179329e1c77efe6648d
],debug=True)
