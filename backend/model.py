#!/bin/python

from config import db

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
	__tablename__ = "member"
	id = db.Column(db.Integer,primary_key=True)
	role = db.Column( db.String(64),unique=True)
	name = db.Column( db.String(64), unique=True)

	def __repr__(self):
		return '<Member:%s, Role:%s>' % (self,name,self.role)

class Partner(db.Model):
	__tablename__ = "partner"
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(64),unique=True)
	logo = db.Column(db.Text,unique=True)
	url = db.Column(db.Text,unique=True) # url for company

	def __repr__(self):
		return '<Partner: %s >' % self.name
