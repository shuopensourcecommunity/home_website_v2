from flask import Flask
from flask import render_template
from flask.views import View
from flask.views import MethodView

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
	rv.row_factory = sqlite3.Row
	return rv


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
