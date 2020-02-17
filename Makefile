# superfluous Makefile to pacify BAndrew and Colin

THESIS = thesis

all: $(THESIS).pdf

$(THESIS).pdf:
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make $(THESIS).tex

clean:
	latexmk -c

cleaner:
	latexmk -CA
