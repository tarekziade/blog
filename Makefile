
build:
	virtualenv --no-site-packages .
	bin/pip install pelican
	bin/pip install markdown

blog:
	bin/pelican -s settings.py
