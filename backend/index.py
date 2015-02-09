from flask import Flask
app = Flask(__name__)
app.debug = True


'''
url rules:
	/    : home
	/home: home

	/general :  a bref introduce to our community

	/activity : student activities

	/project:  community project

	/contact:  contanct us

'''


@app.route('/')
def hello_world():
	return "Hello World!"

if __name__ == '__main__':
	app.run()
