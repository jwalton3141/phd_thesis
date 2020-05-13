#!/usr/bin/env python3

"""
Produce plots which aim to illustrate the importance of running multiple
chains to assess convergence.
"""

import sys
sys.path.insert(0, '..')
import numpy as np
import matplotlib.pyplot as plt

from pretty import set_size, savefig


def between_var(iters):
    """
    Produce a plot which illustrates two chains which have large between-chain
    variance, but small within-chain variance.
    """
    fig, ax = make_fig_ax()

    y1 = np.random.normal(size=iters)
    y2 = np.random.normal(loc=7, size=iters)

    ax.plot(range(iters), y1)
    ax.plot(range(iters), y2)
    tidy_ax(ax, iters)

    ax.set_ylabel(r'$\theta$')

    fig.savefig('B.pdf', format='pdf', bbox_inches='tight')


def within_var(iters):
    """
    Produce a plot which illustrates two chains which have large within-chain
    variance, but small between-chain variance.
    """
    fig, ax = make_fig_ax()

    y1 = (np.random.normal(size=iters, scale=1)
          - np.r_[:iters] / 100)
    y2 = (np.random.normal(loc=y1[-1], size=iters, scale=1)
          + np.r_[:iters] / 100)

    ax.plot(range(iters), y1)
    ax.plot(range(iters), y2)
    tidy_ax(ax, iters)

    fig.savefig('W.pdf', format='pdf', bbox_inches='tight')


def make_fig_ax():
    """Lazy function to control figure and ax size in plots."""
    return plt.subplots(1, 1, figsize=set_size(fraction=0.5))


def tidy_ax(ax, iters):
    """Tidy up the labels and limits of ax."""
    ax.set_xlabel('')
    ax.set_xlim(0, iters)
    ax.set_xticks([0, iters // 2, iters])
    ax.set_xticklabels(['$0$', r'{\normalsize iteration}','$n$'])
    ax.set_yticks([])


def main():
    iters = 500
    between_var(iters)
    within_var(iters)


if __name__ == "__main__":
    main()

