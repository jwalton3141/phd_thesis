# superfluous Makefile to pacify BAndrew and Colin

THESIS = thesis

# Always run latexmk
.PHONY: $(THESIS).pdf all clean

all: $(THESIS).pdf

$(THESIS).pdf: $(THESIS).tex
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make $(THESIS).tex

clean:
	latexmk -c

cleaner:
	latexmk -CA
