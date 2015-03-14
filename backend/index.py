from flask import Flask
from flask import render_template
from flask.views import View
from flask.views import MethodView
from flask import g
import sqlite3,os
from flask.ext.sqlalchemy import SQLAlchemy
from activityAPI import ActivityAPI
basedir = os.path.abspath( os.path.dirname(__file__))
app = Flask(__name__)
app.debug = True

#Use sqlite to test envirment
app.config['SQLALCHEMY_DATABASE_URI'] = \
		'sqlite:///'+ os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


@app.route('/')
def index():
	return "This is api backend"


activity_view = ActivityAPI.as_view('activity_api')
app.add_url_rule('/activity/<int:user_id>/<string:resource>',defaults={},
		view_func = activity_view, methods=['GET',])



class Activity(db.Model):
	__tablename__ = "activity"
	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(64),unique=True)
	time = db.Column(db.DateTime,unique=True)
	location = db.Column(db.String(64),unique=True)
	content = db.Column(db.Text,unique=True)
	photo = db.Column(db.Text,unique=True)

	def __repr__(self):
		return '<Activity %r>' % self.title


class Project(db.Model):
	__tablename__ = "project"
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(64),unique=True)
	intro = db.Column(db.Text,unique=True)
	top = db.Column(db.Boolean,default=False)
	time = db.Column(db.DateTime,unique=True)
	developer = db.Column(db.Text,unique=True)
	link = db.Column(db.Text,unique=True)


	def __repr__(self):
		return '<Project: %s>' % self.name 

class Member(db.Model):
	__tablename__ = "project"
	id = db.Column(db.Integer,primary_key=True)
	role = db.Column( db.String(64),unique=True)
	name = db.Column( db.String(64), unique=True)

	def __repr__(self):
		return '<Member:%s, Role:%s>' % (self,name,self.role)

class Partner(db.Model):
	__tablename__ == "partner"
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(64),unique=True)
	logo = db.Column(db.Text,unique=True)
	url = db.Column(db.Text,unique=True) # url for company

	def __repr__(self):
		return '<Partner: %s >' % self.name

if __name__ == '__main__':
	app.run()
