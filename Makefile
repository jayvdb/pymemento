all: test dist

dist:
	python setup.py sdist --formats=bztar,gztar,zip
	python setup.py bdist_egg

test:
	(cd pymemento/test && python -m unittest discover)

manifest:
	python setup.py sdist --manifest-only

install:
	python setup.py install

clean:
	-rm -rf dist
	-rm MANIFEST
	-rm -rf build
	-rm -rf pymemento.egg-info
	-find . -type f -name '*.pyc' -exec rm {} \;
	-find . -type d -name '__pycache__' -exec rm -rf {} \;
