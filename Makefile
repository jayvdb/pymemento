all: test dist

dist:
	python setup.py sdist --formats=bztar,gztar,zip

test:
	@echo "Testing not implemented yet"

manifest:
	python setup.py sdist --manifest-only

clean:
	-rm -rf dist
	-rm MANIFEST
