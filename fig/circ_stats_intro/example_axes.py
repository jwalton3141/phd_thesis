#! /usr/bin/env python3

"""Script to generate plots which compare different angle measuring conventions."""

import sys
sys.path.insert(0, '..')
import matplotlib.pyplot as plt

from pretty import set_size, savefig


def main():
    """Do the plot thing."""
    # Degree plot
    fig1, ax1 = make_fig_ax()

    tick_labels = [r'$360^\circ, 0^\circ$',
                   r'$45^\circ$',
                   r'$90^\circ$',
                   r'$135^\circ$',
                   r'$180^\circ$',
                   r'$225^\circ$',
                   r'$270^\circ$',
                   r'$315^\circ$']
    plot(fig1, ax1, tick_labels)

    fig1.subplots_adjust(left=1 - fig1.subplotpars.right)
    savefig(fig1, "degree_axes", tight=None)

    # Radian plot
    fig2, ax2 = make_fig_ax()

    tick_labels = [r'$0$',
                   r'$\pi/4$',
                   r'$\pi/2$',
                   r'$3\pi/4$',
                   r'$-\pi, \pi$',
                   r'$-3\pi/4$',
                   r'$-\pi/2$',
                   r'$-\pi/4$']
    plot(fig2, ax2, tick_labels)

    # Can't really work out what I was doing here but looks orite
    fig2.subplots_adjust(right=fig1.subplotpars.right, left=fig1.subplotpars.left)
    savefig(fig2, "radian_axes", tight=None)


def make_fig_ax():
    """Set up polar figure and axes to plot on."""
    fig, ax = plt.subplots(1, 1,
                           figsize=set_size(fraction=0.5, aspect='equal'),
                           subplot_kw=dict(projection='polar'))
    ax.yaxis.grid(False)
    ax.set_yticks([])

    return fig, ax


def plot(fig, ax, tick_labels):
    """Set the tick labels and pad."""
    ax.set_xticklabels(tick_labels)
    fig.tight_layout(pad=0.1)


if __name__ == "__main__":    
    main()

