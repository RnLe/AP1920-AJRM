all: build/main.pdf

# hier Python-Skripte:
plots/plot.pdf: python/plot.py python/matplotlibrc python/header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot.py -up

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: plots/plot.pdf

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
