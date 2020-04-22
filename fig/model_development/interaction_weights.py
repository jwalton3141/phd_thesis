#!/usr/bin/env python3

"""Produce plots showing interaction weighting kernel for metric models."""

import sys
sys.path.insert(0, '..')
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from pretty import set_size, savefig


def equate_y_lims(ax):
    """Ensure all axes have the same y-limits."""
    ax.set_ylim(-0.1, 1.1)


def vicsek(ax):
    """Plot the interaction kernel from OG Vicsek model."""

    # Weighting
    ax.hlines(1, 0, 0.5, color='C0')
    ax.hlines(0, 0.5, 1, color='C0')

    # Show discontinuity
    ax.vlines(0.5, 0, 1, color='C0', linestyle='--')

    ax.set_xticks([0, 0.5, 1])
    ax.set_xticklabels(['$0$', '$r$', '$2r$'])
    
    ax.set_yticks([0, 0.5, 1])
    # Make axis label inline with tickdata, for extra space
    ax.set_yticklabels(['$0$', '$\omega_{ij,t}$', '$1$'])

    # Roate and resize the omega label
    for label in ax.get_yticklabels():
        if len(label._text) > 5:
            label.set_rotation(90)  
            label.set_fontsize(10)

    # ylabel is inline
    ax.set_ylabel('')
    ax.set_xlabel(r'$d_{ij,t}$')

    equate_y_lims(ax)
    ax.set_xlim(0, 1)


def power_law(ax):
    """Plot the interaction kernel for the power-law weighted model."""
    ax.scatter(0, 1, c='C0')

    x = np.linspace(0, 10)
    ax.plot(x, x**-1)

    ax.set_xlabel(r'$d_{ij,t}$')

    ax.set_xticks([0, 10])
    ax.set_xticklabels(['$0$', '$d$'])

    equate_y_lims(ax)
    ax.set_yticks([])
    ax.set_xlim(-0.4, 10)
    


def gaussian(ax):
    """Plot the interaction kernel for the Gaussian weighted model."""
    ax.set_xlabel(r'$d_{ij,t}$')
    equate_y_lims(ax)

    x = np.linspace(0, 1.5)
    sd = 0.4

    ax.plot(x, norm.pdf(x, scale=sd), c='C0')

    ax.set_xticks([0, 2 * sd])
    ax.set_xticklabels(['$0$', r'$2\,\sigma_X$'])
    ax.vlines(2*sd, 0, norm.pdf(2*sd, scale=sd),
              color='C0', linestyle='--')

    ax.set_yticks([])
    ax.set_xlim(0, 1.5)    


def main():
    """Make the plot."""
    figsize = set_size()
    # Ignore my over-engineered plot dimension considerations
    figsize[1] = 2
    fig, ax = plt.subplots(1, 3, figsize=figsize)

    # Plot kernels on seperate axes
    for axi, fun, in zip(ax, [vicsek, power_law, gaussian]):
        fun(axi)

    # Adjust spacing a little
    fig.subplots_adjust(left=0.05,
                        right=1,
                        top=0.99,
                        bottom=0.25)
    fig.savefig('weighting_rules.pdf', format='pdf')


if __name__ == "__main__":
    main()

