from flask import Flask
from flask import render_template
from flask.views import MethodView

app = Flask(__name__)

app.debug = True


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/acitivies/title',methods=['GET','POST'])
def get_activity_title():
	if request.method == 'GET':
		# get title as a dictionary
		title = {}
		body = flask.jsonify(**title)

		return flask.jsonify(**title)


@app.errorhandler(404)
def not_found(error):
	pass


if __name__ == '__main__':
	app.run()
