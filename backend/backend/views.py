from backend import app,db
from api import ActivityAPI,ProjectAPI,MemberAPI,PartnerAPI
# add url rules for models
app.add_url_rule('/activity/<int:user_id>/<string:resource>',defaults={},view_func = ActivityAPI.as_view('activity_view'), methods=['GET',])
app.add_url_rule('/project/<int:project_id>/<string:resource>',defaults={},view_func = ProjectAPI.as_view('project_view'),methods=['GET',])
app.add_url_rule('/member/<int:member_id>/<string:resource>',defaults={},view_func = MemberAPI.as_view('member_view'),methods=['GET',])
app.add_url_rule('/partner/<int:partner_id>/<string:resource>',defaults={},view_func = PartnerAPI.as_view('partner_view'),methods=['GET',])




@app.route('/')
def index():
	return "This is api backend"