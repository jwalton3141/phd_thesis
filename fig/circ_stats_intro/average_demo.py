#! /usr/bin/env python3

"""Illustrate the circular and arithmetic mean for data."""

import sys
sys.path.insert(0, '..')
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np

from pretty import set_size, savefig


def main():
    """Plot and save desired graph."""
    fig, ax = make_fig_ax()
    plot_arith_mean(fig, ax)
    savefig(fig, 'arith_mean', tight=None)

    fig, ax = make_fig_ax()
    plot_circ_mean(fig, ax)
    savefig(fig, 'circ_mean', tight=None)


def make_fig_ax():
    """Make polar figure and axes to plot on."""
    fig, ax = plt.subplots(1, 1,
                           figsize=set_size(fraction=0.5, aspect='equal'),
                           subplot_kw=dict(projection='polar'))

    # Turn off radial grid
    ax.grid(False)
    # Remove radius marks
    ax.set_yticks([])
    # Only plot half of degree tick labels
    ax.set_xticks(ax.get_xticks()[::2])

    tick_labels = ax.get_xticklabels()
    # Change 0 label to show 0 AND 360
    tick_labels[0].set_text('$360^\\circ, 0^\\circ$')
    ax.set_xticklabels(tick_labels)

    return fig, ax


def setup_plot(ax):
    """Illustrations for the arithmetic mean and circular mean have the same setup."""
    colour = 'C0'

    ax.plot([0, 10 * np.pi / 180],
            [0, 0.9],
            c=colour,
            lw=2)

    ax.plot([0, 350 * np.pi / 180],
            [0, 0.9],
            c=colour,
            lw=2)

    add_arrow(ax, colour, 10)

    add_arrow(ax, colour, 350)


def add_arrow(ax, colour, angle):
    # Bug in plotting arrows on polar plot. Work around is to plot at 0 and transform
    ax.arrow(0, 0, 0, 1,
             color=colour,
             linewidth=1,
             width=0.01,
             length_includes_head=True,
             transform=mtransforms.Affine2D().translate(angle * np.pi / 180, 0) + ax.transData,
             head_width=0.08)


def plot_arith_mean(fig, ax):
    """Plot the arithmetic mean of 350 and 10."""
    setup_plot(ax)

    colour = 'C2'
    ax.plot([0, np.pi], [0, 0.9], c=colour, lw=2)
    add_arrow(ax, colour, 180)
    adjust_plots(fig, ax)


def plot_circ_mean(fig, ax):
    """Plot the circular mean of 350 and 10."""
    setup_plot(ax)

    colour = 'C1'
    ax.plot([0, 0], [0, 0.9], c=colour, lw=2)
    add_arrow(ax, colour, 0)
    adjust_plots(fig, ax)


def adjust_plots(fig, ax):
    """Make final adjustments to padding and limits of plots."""
    ax.set_ylim([0, 1.05])
    fig.tight_layout(pad=0.1)
    fig.subplots_adjust(left=1 - fig.subplotpars.right)


if __name__ == "__main__":
    main()

