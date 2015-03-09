#!/bin/python

from flask.views import MethodView

class ActivityAPI(MethodView):
	def get(self):
		return "this is get"
	def post(self):
		pass
	def delete(self):
		pass
	def put(self):
		pass
