#! /bin/bash
COUNT=$(detex -l -e equation,table,algorithm,align,figure thesis.tex | tr '\n' ' ' | sed 's/*//g' | wc -w)
echo Word count: $COUNT
