from fabric.api import *

env.user = 'ubuntu'

env.hosts = ['api.shuosc.org']

def pack():
	local('python setup.py sdist --formats=gztar',capture=False)


def deploy():
	dist = local('python setup.py --fullname',capture=True).strip()

	put('dist/%s.tar.gz'%dist,'/tmp/backend.tar.gz')

	run('mkdir /tmp/backend')

	with cd('/tmp/backend'):
		run('tar xvf /tmp/backend.tar.gz')
		run('/var/www/shuosc/backend/venv/bin/python setup.py install')
	run('rm -rf /tmp/backend /tmp/backend.tar.gz')
	run('touch /var/www/shuosc/backend/shuosc_uwsgi.sock')	
