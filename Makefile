# A Makefile for compiling LaTeX documents.
#------------------------------------------------------------------------------
OBJECT		= thesis
BIBTEX		= true
LATEX		= pdflatex
TEXSOURCES	= $(OBJECT).tex $(wildcard *.tex) $(wildcard ./*/*.tex)
SOURCES		= $(TEXSOURCES) inputs/masthesis.sty
.SUFFIXES: .tex .dvi .ps .pdf .ps.gz .bbl .dat

$(OBJECT).pdf: $(OBJECT).bbl $(OBJECT).tex $(SOURCES)
	$(LATEX) -shell-escape $* --enable-write18
	$(LATEX) -shell-escape $* --enable-write18
	@ inputs/spell_check.sh
    # Open thesis if NOT compiling in ssh session
	@ inputs/openif.sh

$(OBJECT).bbl: $(OBJECT).tex references.bib $(SOURCES)
	$(LATEX) -shell-escape $* --enable-write18
	$(BSTINPUTS) bibtex $*

default: $(OBJECT).pdf

tidy:
	rm -f *.aux *.toc *.log *.out  *.bbl *.blg *.idx *.lot *.lof */*.aux
clean: tidy
	rm -f $(OBJECT).dvi $(OBJECT).synctex.gz $(OBJECT)-compress.pdf $(OBJECT).pdf $(OBJECT)-figure*.pdf $(OBJECT)-figure*.dep $(OBJECT)-figure*.dpth $(OBJECT)-figure*.table $(OBJECT)-figure*.gnuplot $(OBJECT).ps
compress:
	 gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/prepress -sOutputFile=$(OBJECT)-compress.pdf $(OBJECT).pdf
spell:
	 @ inputs/spell_check.sh
