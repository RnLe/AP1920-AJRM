all: build/main.pdf

# hier Python-Skripte:
build/main.pdf:: python/plot.py python/matplotlibrc python/header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python python/plot.py -up

build/main.pdf:: python/show_me_da_amplitudes.py
	TEXINPUTS=$$(pwd): python python/show_me_da_amplitudes.py -up

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf:: plots/amplitudes_steel_close(t7).pdf plots/plot_steel_dynamic200.pdf plots/plot_tempDiff_brass_wide.pdf plots/amplitudes_brass_wide_far(t1).pdf plots/plot_tempDiff_steel.pdf plots/amplitudes_aluminum_close(t6).pdf plots/plot_t5_t8.pdf plots/amplitudes_aluminum_far(t5).pdf plots/plot_brass_wide_dynamic40.pdf plots/plot_t1_t4.pdf plots/amplitudes_brass_wide_close(t2).pdf plots/plot_aluminum_dynamic40.pdf | build
	TEXINPUTS=$$(pwd): python python/plot.py -up
	TEXINPUTS=$$(pwd): python python/show_me_da_amplitudes.py -up

build/main.pdf:: FORCE | build
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
