## Spell check

Spell checking in TexMaker leaves much to be desired as it flags the contents of LaTex commands such as \ref, \cite, etc. So I've added a custom spell checker - which ignore LaTex commands - to run at compile time

Aspell is used to check the spelling of the chapters. Compile the thesis and perform a spell check by running
```/path/to/thesis$ make```. A list of misspelt words and the containing chapter will be printed to stdout.

To add words to the Aspell dictionary append to ```inputs/custom_spellings```. To add LaTex commands to ignore append
to ```inputs/ignore_tex```.
