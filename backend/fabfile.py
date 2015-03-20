from fabric.api import *

env.user = 'ubuntu'

env.hosts = ['api.shuosc.org']

def pack():
	local()


def deploy():
	pass
