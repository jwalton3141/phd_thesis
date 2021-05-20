[![Build Thesis](https://github.com/jwalton3141/phd_thesis/actions/workflows/main.yml/badge.svg)](https://github.com/jwalton3141/phd_thesis/actions/workflows/main.yml)

# Bayesian Inference for Models of Collective Behaviour

I submitted my thesis to Newcastle University's department of Maths, Stats &
Physics in December 2020.

[Dr. Richard P. Mann](http://www.richardpmann.com/) performed the role of
external examiner, and [Dr. Nick
Parker](https://www.ncl.ac.uk/maths-physics/people/profile/nickparker.html)
performed that of the internal examiner.

# Building

You will require an install of `texlive-full` to build this thesis. To build,
clone and then run `make`:

```sh
git clone git@github.com:jwalton3141/phd_thesis.git &&
    cd phd_thesis &&
    make
```

## Fonts

I used the luxurious [MinionPro font](https://fonts.adobe.com/fonts/minion)
(for which you need a license to use) for submission. Without Minion Pro the
built pdf will look different to my submitted copy.

To install MinionPro run `./scripts/make_minion.sh`. The script does *not*
require root privileges, but it does require an install of [LCDF
typetools](http://www.lcdf.org/type/) and a complete TeXLive or MiKTeX install.
This script need only be run once. Before you install and use this font ensure
that you have a license to do so. 

## Cite me

```tex
@Thesis{	  walton2021,
  Author	= {Jack Walton},
  Title		= {Bayesian Inference for Models of Collective Behaviour},
  School	= {University of Newcastle upon Tyne},
  Year		= {2021}
}
```
