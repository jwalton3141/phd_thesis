## Style

I have adapted masthesis.sty to implement my only custom style. We're concerned that this may cause problems further down the line as it departs from the university guidelines. As such I've ensured that everything is backwards compatible and that we can swap back to the offical style with minimal effort if we decide it prudent.

I took much inspiration (and many commands) from [Dave Robertson's attempt](https://mas-gitlab.ncl.ac.uk/b0036119/thesis-template) at recreating [Aaron Turin's thesis](https://people.mpi-sws.org/~turon/turon-thesis.pdf).

## Font

Text is typeset with MinionPro. To install it on your system follow the instructions at https://github.com/sebschub/FontPro. Otherwise, to compile without the font simply comment out ```\usepackage{MinionPro}``` in ```inputs/masthesis.sty``` and ```fig/*.tikz```.

## Spell check

Spell checking in TexMaker leaves much to be desired as it flags the contents of LaTex commands such as \ref, \cite, etc. So I've added a custom spell checker - which ignore LaTex commands - to run at compile time

Aspell is used to check the spelling of the chapters. Compile the thesis and perform a spell check by running
```/path/to/thesis$ make```. A list of misspelt words and the containing chapter will be printed to stdout.

To add words to the Aspell dictionary append to ```inputs/custom_spellings```. To add LaTex commands to ignore append
to ```inputs/ignore_tex```.
