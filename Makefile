
build:
	python3 -m venv .
	bin/pip install pelican
	bin/pip install markdown

blog:
	bin/pelican -s settings.py
