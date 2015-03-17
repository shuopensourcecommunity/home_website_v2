import model

from flask.views import MethodView
from flask import jsonify
from flask import make_response
class ActivityAPI(MethodView):
	def get(self,*args,**kwargs):
		print self,args,kwargs
		data = model.Activity.query.filter_by(id=kwargs['user_id']).first()
		data_json = { kwargs['resource'] : data.__getattribute__(kwargs['resource'])}
		data_json = jsonify(data_json)
		resp = make_response( data_json,200 )
		return resp
	def post(self):
		pass
	def delete(self):
		pass
	def put(self):
		pass

class ProjectAPI(MethodView):
	def get(self,*args,**kwargs):
		pass
	def post(self):
		pass
	def delete(self):
		pass
	def put(self):
		pass


class MemberAPI(MethodView):
	def get(self,*args,**kwargs):
		pass
	def post(self):
		pass
	def delete(self):
		pass
	def put(self):
		pass


class PartnerAPI(MethodView):
	def get(self,*args,**kwargs):
		pass
	def post(self):
		pass
	def delete(self):
		pass
	def put(self):
		pass
