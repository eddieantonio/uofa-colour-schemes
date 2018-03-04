PATH := $(PATH):.

SCHEMES := $(wildcard *.tsv)
CSS := $(SCHEMES:.tsv=.css)

all: $(CSS)

%.css: %.tsv scheme2css
	scheme2css $< > $@

.PHONY: all
