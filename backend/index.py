from flask import Flask
from flask import render_template
from flask.views import View
from flask.views import MethodView
from flask import g
import sqlite3
# import models
from activityModel import ActivityAPI

app = Flask(__name__)
app.debug = True

#import database config
app.config.from_pyfile('./test_database/config.cfg')

def connect_db():
	''' 
	Connects to the database
	'''
	rv = sqlite3.connect( app.config['DATABASE'] )
	return rv

@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	if hasattr(g,'db'):
		g.db.close()



@app.route('/')
def index():
	print app.config['DATABASE']
	return "This is api backend"

@app.errorhandler(404)
def not_found(error):
	pass

activity_view = ActivityAPI.as_view('activity_api')
app.add_url_rule('/activity/',defaults={},
		view_func = activity_view, methods=['GET',])


if __name__ == '__main__':
	app.run()
