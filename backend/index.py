from config import app
from api import ActivityAPI,ProjectAPI

# add url rules for models
app.add_url_rule('/activity/<int:user_id>/<string:resource>',defaults={},
				view_func = ActivityAPI.as_view('activity_view'), methods=['GET',])
app.add_url_rule('/project/<int:project_id>/<string:resource>',defaults={},
				view_func = ProjectAPI.as_view('project_view'),methods=['GET',])




@app.route('/')
def index():
	return "This is api backend"


if __name__ == '__main__':
	app.run()
