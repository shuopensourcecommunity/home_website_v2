from fabric.api import *
from fabtools import require
env.user = 'ubuntu'
env.port = 3868

env.hosts = ['api.shuosc.org']



def pack():
	local('python setup.py sdist --formats=gztar',capture=False)


def deploy():
	dist = local('python setup.py --fullname',capture=True).strip()

	put('dist/%s.tar.gz'%dist,'/tmp/backend.tar.gz')
	run('mkdir /tmp/backend')

	run('tar xvf /tmp/backend.tar.gz -C /tmp/backend')
	run('cd /tmp/backend/'+dist)
	run('ls -al')
	sudo('/var/www/shuosc/backend/venv/bin/python /tmp/backend/'+dist+'/setup.py install --prefix=/var/www/shuosc/backend', user='www-data')
	run('rm -rf /tmp/backend /tmp/backend.tar.gz')
	run('touch /var/www/shuosc/backend/shuosc_uwsgi.sock')	

