#!/usr/bin/env python3

"""Produce plots showing interaction weighting kernel for metric models."""

import sys
sys.path.insert(0, '..')
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from pretty import set_size, savefig


def adjust_fig(fig):
    fig.subplots_adjust(top=1,
                        bottom=0.25,
                        left=0.1,
                        right=0.9)


def equate_y_lims(ax):
    """Ensure all axes have the same y-limits."""
    ax.set_ylim(-0.1, 1.1)


def vicsek(fig, ax):
    """Plot the interaction kernel from OG Vicsek model."""

    # Weighting
    ax.hlines(1, 0, 0.5, color='C0')
    ax.hlines(0, 0.5, 1, color='C0')

    # Show discontinuity
    ax.vlines(0.5, 0, 1, color='C0', linestyle='--', alpha=0.5)

    ax.set_xticks([0, 0.5])
    ax.set_xticklabels(['$0$', '$r$'])
    
    ax.set_yticks([0, 0.5, 1])
    # Make axis label inline with tickdata, for extra space
    ax.set_yticklabels(['$0$', '$\omega_{ij,t}$', '$1$'])

    # Roate and resize the omega label
    for label in ax.get_yticklabels():
        if len(label._text) > 5:
            label.set_va('center')
            label.set_rotation(90)  
            label.set_fontsize(10)

    # ylabel is inline
    ax.set_ylabel('')
    ax.set_xlabel(r'$d_{ij,t}$')

    equate_y_lims(ax)
    ax.set_xlim(0, 1)
    adjust_fig(fig)
    fig.savefig('vicsek_weighting.pdf')


def power_law(fig, ax):
    """Plot the interaction kernel for the power-law weighted model."""
    ax.scatter(0, 1, c='C0')

    x = np.linspace(0, 10)
    ax.plot(x, x**-1)

    ax.set_xlabel(r'$d_{ij,t}$')

    ax.set_xticks([0, 10])
    ax.set_xticklabels(['$0$', '$d$'])

    equate_y_lims(ax)
    ax.set_yticks([0, 1])
    ax.set_xlim(-0.4, 10)
    adjust_fig(fig)
    fig.savefig('power_weighting.pdf')


def gaussian(fig, ax):
    """Plot the interaction kernel for the Gaussian weighted model."""
    ax.set_xlabel(r'$d_{ij,t}$')
    equate_y_lims(ax)

    x = np.linspace(0, 1.5)
    sd = 0.4

    ax.plot(x, norm.pdf(x, scale=sd), c='C0')

    ax.set_yticks([0, 0.5, 1])
    # Make axis label inline with tickdata, for extra space
    ax.set_yticklabels(['$0$', '$\omega_{ij,t}$', '$1$'])
    ylims = ax.get_ylim()

    ax.set_xticks([0, 2 * sd])
    ax.set_xticklabels(['$0$', r'$2\,\sigma_X$'])
    ax.vlines(2*sd,
              ylims[0],
              norm.pdf(2*sd, scale=sd),
              color='C0',
              linestyle='--',
              alpha=0.5)
    ax.set_ylim(ylims)

    # Roate and resize the omega label
    for label in ax.get_yticklabels():
        if len(label._text) > 5:
            label.set_va('center')
            label.set_rotation(90)  
            label.set_fontsize(10)

    ax.set_xlim(0, 1.5)    
    adjust_fig(fig)
    fig.savefig('gaussian_weighting.pdf')


def topological(fig, ax):
    """Plot the interaction kernel for our topological model."""
    ax.set_xticks(range(6))
    ax.set_yticks(range(3))

    partial_weight = 0.4

    ax.scatter([0, 1, 3, 4, 5],
               [1, 1, 1, partial_weight, 0],
               marker='x')

    ax.set_xlabel('$n$-th closest neighbour')

    ax.set_xticks([0, 1, 2, 3, 4, 5])
    ax.set_xticklabels(['$1$',
                        '$2$',
                        r'$\ldots$',
                        r'$\lfloor k \rfloor$',
                        r'$\lceil k \rceil$',
                        r'$\lceil k \rceil$+1'])

    ax.set_yticks([0, partial_weight, 1])
    ax.set_yticklabels(['$0$',
                        r'$k - \lfloor k \rfloor$',
                        '$1$'])

    xlims = ax.get_xlim()
    ylims = ax.get_ylim()
    ax.hlines(1, 
              xlims[0],
              3,
              color='C0',
              linestyle='--',
              alpha=0.5)
    ax.hlines(partial_weight, 
              xlims[0],
              4,
              color='C0',
              linestyle='--',
              alpha=0.5)
    ax.hlines(0, 
              xlims[0],
              5,
              color='C0',
              linestyle='--',
              alpha=0.5)
    ax.vlines([0, 1, 3],
              [1] * 3,
              ylims[0] * 3,
              color='C0',
              linestyle='--',
              alpha=0.5)
    ax.vlines(4,
              partial_weight,
              ylims[0] - 1,
              color='C0',
              linestyle='--',
              alpha=0.5)
    ax.vlines(5,
              0,
              ylims[0] - 1,
              color='C0',
              linestyle='--',
              alpha=0.5)
    ax.set_xlim(xlims)
    ax.set_ylim(ylims)

    for label in ax.get_yticklabels():
        if len(label._text) > 5:
            label.set_va('center')
            label.set_rotation('vertical')
            

    equate_y_lims(ax)
    adjust_fig(fig)
    fig.savefig('topological_weighting.pdf')


def make_fig_ax():
    return plt.subplots(1, 1, figsize=set_size(fraction=0.5))


def main():
    """Make the plot."""

    for fun in [vicsek, power_law, gaussian, topological]:
        fig, ax = make_fig_ax() 
        fun(fig, ax)

    # fig.savefig('weighting_rules.pdf', format='pdf')


if __name__ == "__main__":
    main()

