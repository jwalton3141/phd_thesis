#! /usr/bin/env python3

"""Plot quadrants of R2 and the correction term which atan2 adds to atan."""

import sys
sys.path.insert(0, '..')
import matplotlib.pyplot as plt

from pretty import set_size, savefig


def main():
    """Plot and save desired graph."""
    fig, ax = plt.subplots(1, 1,
            figsize=set_size(fraction=0.7, aspect='equal'))

    add_axis(ax)

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    shade_quadrants(ax)
    annotate_quadrants(ax)

    ax.set_aspect('equal')
    savefig(fig, 'atan_quadrants')


def add_axis(ax):
    """Add x and y axis to figure."""
    # y axis
    ax.arrow(0, -1, 0, 2,
            length_includes_head=True,
            width=0.005,
            head_width=0.04,
            color='k',
            alpha=0.8)
    # x axis
    ax.arrow(-1, 0, 2, 0,
            length_includes_head=True,
            width=0.005,
            head_width=0.04,
            color='k',
            alpha=0.8)

    # Remove ticks on axes
    ax.set_xticks([])
    ax.set_yticks([])

    # Add x and y axis labels
    ax.text(0.9, 0.1, '$x$',
            horizontalalignment='center',
            verticalalignment='center')
    ax.text(0.1, 0.9, '$y$',
            horizontalalignment='center',
            verticalalignment='center')


def shade_quadrants(ax):
    """Shade the four quadrants according to how they are treated by atan2."""
    # Shade x > 0
    ax.fill([0, 1, 1, 0],
            [-1, -1, 1, 1],
            'C0', alpha=0.8)

    # Shade x < 0, y > 0
    ax.fill([0, -1, -1, 0],
            [0, 0, 1, 1],
            'C1', alpha=0.8)

    # Shade x < 0, y < 0
    ax.fill([0, -1, -1, 0],
            [-1, -1, 0, 0],
            'C2', alpha=0.8)


def annotate_quadrants(ax):
    """Add the formula for atan2 in each of the four quadrants."""
    ax.text(0.5, 0.5, r'atan$(y/x)$',
            horizontalalignment='center',
            verticalalignment='center')

    ax.text(0.5, -0.5, r'atan$(y/x)$',
            horizontalalignment='center',
            verticalalignment='center')

    ax.text(-0.5, 0.5, r'atan$(y/x) + \pi$',
            horizontalalignment='center',
            verticalalignment='center')

    ax.text(-0.5, -0.5, r'atan$(y/x) - \pi$',
            horizontalalignment='center',
            verticalalignment='center')


if __name__ == "__main__":
    main()

