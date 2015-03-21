from setuptools import setup,find_packages
setup(

		name = "backend",
		version = "1.0",
		long_description=__doc__,
		packages = find_packages(),
		include_package_data=True,
		zip_safe = False,
		install_requires=[
			'Flask>=0.10.1',
			'Fabric>=1.10.1',
			'ecdsa>=0.13',
			'Flask-SQLAlchemy>=2.0',
			'itsdangerous>=0.24',
			'Jinja2>=2.7.3',
			'MarkupSafe>=0.23',
			'paramiko>=1.15.2',
			'pycrypto>=2.6.1',
			'SQLAlchemy>=0.9.8',
			'Werkzeug>=0.10.1'
		]
)

