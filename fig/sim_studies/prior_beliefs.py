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
    figsize[1] = 2

    fig, ax = plt.subplots(1, 3, figsize=figsize)

    [ax[i].set_ylabel('') for i in [1, 2]]
    ax[0].set_ylabel('density')

    labels = ['$r$', r'$\sigma_Y$', r'$\nu$']
    [ax[i].set_xlabel(lab) for i, lab in enumerate(labels)]

    x = np.linspace(20, 60, num=100)
    ax[0].plot(x, gamma.pdf(x, gamma.pdf(x, a=50, scale=5)))
    ax[0].set_xlim(20, 60)

    x = np.linspace(0.02, 0.15, num=100)
    ax[1].plot(x, gamma.pdf(x, gamma.pdf(x, a=2, scale=1 / 100)))
    ax[1].set_xlim(0.02, 0.15)

    x = np.linspace(0, 10, num=100)
    ax[2].plot(x, gamma.pdf(x, gamma.pdf(x, a=2, scale=1 / 0.1)))
    ax[2].set_xlim(0, 10)

    fig.subplots_adjust(top=0.925,
                        bottom=0.215,
                        right=0.98,
                        left=0.08,
                        wspace=0.35)

    fig.savefig('priors.pdf')


if __name__ == "__main__":
    main()
