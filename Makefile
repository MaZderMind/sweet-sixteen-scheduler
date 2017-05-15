all: webdriver-ui

dependencies:
	cd lib/driver/webdriver-static && npm install

webdriver-ui: dependencies
	cd lib/driver/webdriver-static && ./node_modules/less/bin/lessc display.less display.css

run:
	python test.py
