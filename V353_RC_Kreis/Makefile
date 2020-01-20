pythons := $(wildcard **/*plot*.py)						# get all python files with the name 'plot' in it to create targets
pdfs := $(patsubst %.py, %.pdf, $(pythons))				# create targets from python files by replacing .py with .pdf
pdfs := $(patsubst python/%, plots/%, $(pdfs))			# create targets from python files by replacing .py with .pdf

all: build/main.pdf

.SECONDEXPANSION:
$(pdfs): $$(patsubst plots%, python%, $$(basename $$@)).py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python $<
	touch $@

build/main.pdf: $(pdfs)

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
