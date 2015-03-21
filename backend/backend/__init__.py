from flask import Flask
from flask import render_template
from flask.views import View
from flask.views import MethodView
from flask import g
import sqlite3,os
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Init of database
#Use sqlite to test envirment
basedir = os.path.abspath( os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
		'sqlite:///'+ os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

import backend.views
