#!/bin/python
class Activity(db.Model):
	__tablename__ = "activity"
	id = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(64),unique=True)
	time = db.Column(db.DateTime,unique=True)
	location = db.Column(db.String(64),unique=True)
	content = db.Column(db.Text,unique=True)
	photo = db.Column(db.Text)
