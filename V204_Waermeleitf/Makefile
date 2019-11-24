all: build/main.pdf

# hier Python-Skripte:
build/plot_t1_t4.pdf build/plot_t5_t8.pdf build/plot_tempDiff_t7t8.pdf build/plot_tempDiff_t2t1.pdf: plot.py matplotlibrc header-matplotlib.tex Messung_1(statisch).txt Messung_2(dynamisch).txt Messung_3(dynamisch).txt | build
	TEXINPUTS=$$(pwd): python plot.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot_t1_t4.pdf build/plot_t5_t8.pdf build/plot_tempDiff_t7t8.pdf build/plot_tempDiff_t2t1.pdf

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
