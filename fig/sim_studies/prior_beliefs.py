#!/usr/bin/env python3

"""Produce plots showing interaction weighting kernel for metric models."""

import sys
sys.path.insert(0, '..')
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

from pretty import set_size, savefig


def main():
    figsize = set_size()
    # Ignore my over-engineered plot dimension considerations
    figsize[1] = 1.7

    fig, ax = plt.subplots(1, 3, figsize=figsize)

    [ax[i].set_ylabel('') for i in [1, 2]]
    ax[0].set_ylabel('density')

    labels = ['$r$', r'$\sigma_Y$', r'$\nu$']
    [ax[i].set_xlabel(lab) for i, lab in enumerate(labels)]

    lower, upper = 30, 70
    x = np.linspace(lower, upper, num=100)
    ax[0].plot(x, gamma.pdf(x, a=50, scale=1), c='C2')
    ax[0].set_xlim(lower, upper)

    lower, upper = 0, 0.1
    x = np.linspace(lower, upper, num=100)
    ax[1].plot(x, gamma.pdf(x, a=2, scale=1 / 100), c='C2')
    ax[1].set_xlim(lower, upper)

    lower, upper = 0, 75
    x = np.linspace(lower, upper, num=100)
    ax[2].plot(x, gamma.pdf(x, a=2, scale=1 / 0.1), c='C2')
    ax[2].set_xlim(lower, upper)

#    fig.subplots_adjust(top=0.925,
#                        bottom=0.25,
#                        right=0.995,
#                        left=0.09,
#                        wspace=0.35)
    fig.tight_layout(pad=0)

    fig.savefig('priors.pdf')


if __name__ == "__main__":
    main()
