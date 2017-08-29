a python script to read markdown files stored in the content directory and render them into a html website. making this since it is easier to write a simple python script rather than understanding the vastness that is hugo or jekyll. plus its a good coding todo.

## Basic idea:

- everything should be in the one github repo:
- structure:
	- root dir is script file and index.html
	- posts are in a subdirectory called posts or content
	- tag pages go under tag
	- post html files go in root for time being
	- templates, css, site graphics go in another subdirectory called site
	- post images go into images
- content is all in markdown files in a directory called source
- use a template language like jinja2 for the html logic etc
- python script which should be just one file, checks all .md files in that directory and builds html files using the html templates - to start with:
	- index
	- actual post
	- tags
- markdown file is rendered through a parser and inserted into the proper template
- posts have front matter in YAML, since jekyll and hugo use that

Using so far:
- [ruamel.yaml](https://pypi.python.org/pypi/ruamel.yaml) to read front matter (titles, date etc) from the top of each markdown file
- [CommonMark](https://github.com/rtfd/CommonMark-py) to translate markdown into html
- [Jinja2](http://jinja.pocoo.org/docs/2.9/) cause need templates and this one seems kind of popular