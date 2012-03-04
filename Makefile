
build:
	virtualenv --no-site-packages .
	bin/pip install pelican

blog:
	bin/pelican -s settings.py
