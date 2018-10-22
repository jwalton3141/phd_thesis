#! /usr/bin/env python3
""" Plot quadrants of R2 and the correction term which atan2 adds to atan. """

import matplotlib.pyplot as plt
from plot.pretty import set_size, savefig

if __name__ == "__main__":
    fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.65, aspect='equal'))

    # y axis
    ax.arrow(0, -1, 0, 2, length_includes_head=True, width=0.005, head_width=0.04, color='k',
             alpha=0.8)
    # x axis
    ax.arrow(-1, 0, 2, 0, length_includes_head=True, width=0.005, head_width=0.04, color='k',
             alpha=0.8)

    # Remove ticks on axes
    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    # Shade x > 0
    ax.fill([0, 1, 1, 0], [-1, -1, 1, 1], 'C0', alpha=0.8)
    # Shade x < 0, y > 0
    ax.fill([0, -1, -1, 0], [0, 0, 1, 1], 'C1', alpha=0.8)
    # Shade x < 0, y < 0
    ax.fill([0, -1, -1, 0], [-1, -1, 0, 0], 'C2', alpha=0.8)

    # Annotate quadrants
    ax.text(0.5, 0.5, r'atan$(y/x)$', horizontalalignment='center', verticalalignment='center')
    ax.text(0.5, -0.5, r'atan$(y/x)$', horizontalalignment='center', verticalalignment='center')
    ax.text(-0.5, 0.5, r'atan$(y/x) + \pi$', horizontalalignment='center',
            verticalalignment='center')
    ax.text(-0.5, -0.5, r'atan$(y/x) - \pi$', horizontalalignment='center',
            verticalalignment='center')

    # Add x and y axis labels
    ax.text(0.9, 0.1, '$x$', horizontalalignment='center', verticalalignment='center')
    ax.text(0.1, 0.9, '$y$', horizontalalignment='center', verticalalignment='center')
    
    ax.set_aspect('equal')
    savefig('/data/thesis/fig/circ_stats_intro/', 'atan_quadrants')
