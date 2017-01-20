all: dist

dist:
	tangram-bundle tron-style.yaml
	mv tron-style.zip dist/tron-style.zip

	tangram-bundle tron-style-more-labels.yaml
	mv tron-style-more-labels.zip dist/tron-style-more-labels.zip

	tangram-bundle tron-style-no-labels.yaml
	mv tron-style-no-labels.zip dist/tron-style-no-labels.zip

clean:
	rm -rf dist
	mkdir dist

tag:
	git tag  -m 'See CHANGELOG for details.' -a v`cat VERSION`
