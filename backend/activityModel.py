#!/bin/python

from flask import Flask
from flask.views import MethodView
from flask import jsonify
from flask import make_response 
class ActivityAPI(MethodView):
	def get(self):
		data = { "activity_title":"testtitle"}
		resp = make_response( jsonify(data),200)
		return resp
	def post(self):
		pass
	def delete(self):
		pass
	def put(self):
		pass
