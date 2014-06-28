all: test dist

dist:
	python setup.py dist

test:
	echo "Not implemented yet"

clean:
	-rm -rf dist
	rm MANIFEST
