#! /usr/bin/env python3
""" Show why the arithmetic mean is inappropriate for circular data and demonstrate why the circular
 mean is better. 
"""

import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np
from plot.pretty import set_size

if __name__ == "__main__":
    fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.45, aspect='equal'),
                           subplot_kw=dict(projection='polar'))
    # Turn of radial grid
    ax.grid(False)
    # Remove 'radius' marks
    ax.set_yticks([])
    # Only plot half of degree tick labels
    ax.set_xticks(ax.get_xticks()[::2])

    # Hack hack hack
    plt.pause(1)
    tick_labels = ax.get_xticklabels()
    # Change 0 label to show 0 AND 360
    tick_labels[0].set_text('$360^\\circ, 0^\\circ$')
    ax.set_xticklabels(tick_labels)

    # Plot lines first to ensure uniform thickness of arrow tails
    ax.plot([0, 10*np.pi/180], [0, 0.9], c='C0', lw=2)
    ax.plot([0, 350*np.pi/180], [0, 0.9], c='C0', lw=2)
    ax.plot([0, np.pi], [0, 0.9], c='C3', lw=2)

    # Bug in plotting arrows on polar plot. Work around is to plot at 0 and transform
    ax.arrow(0, 0, 0, 1, color='C0', linewidth=1, width=0.01, length_includes_head=True,
         transform=mtransforms.Affine2D().translate(10*np.pi/180, 0) + ax.transData,
         head_width=0.08)
    
    ax.arrow(0, 0, 0, 1, color='C0', linewidth=1, width=0.01, length_includes_head=True,
         transform=mtransforms.Affine2D().translate(350*np.pi/180, 0) + ax.transData,
         head_width=0.08)

    ax.arrow(0, 0, 0, 1, color='C3', linewidth=1, width=0.01, length_includes_head=True,
         transform=mtransforms.Affine2D().translate(np.pi, 0) + ax.transData,
         head_width=0.08)

    ax.set_ylim([0, 1.05])
    fig.tight_layout(pad=0.1)
    fig.subplots_adjust(left=1-fig.subplotpars.right)
    fig.savefig('/data/thesis/fig/circ_stats_intro/arith_mean')

    fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.45, aspect='equal'),
                           subplot_kw=dict(projection='polar'))
    # Turn of radial grid
    ax.grid(False)
    # Remove 'radius' marks
    ax.set_yticks([])
    # Only plot half of degree tick labels
    ax.set_xticks(ax.get_xticks()[::2])

    # Hack hack hack
    plt.pause(1)
    tick_labels = ax.get_xticklabels()
    # Change 0 label to show 0 AND 360
    tick_labels[0].set_text('$360^\\circ, 0^\\circ$')
    ax.set_xticklabels(tick_labels)

    # Plot lines first to ensure uniform thickness of arrow tails
    ax.plot([0, 10*np.pi/180], [0, 0.9], c='C0', lw=2)
    ax.plot([0, 350*np.pi/180], [0, 0.9], c='C0', lw=2)
    ax.plot([0, 0], [0, 0.9], c='C2', lw=2)

    # Bug in plotting arrows on polar plot. Work around is to plot at 0 and transform
    ax.arrow(0, 0, 0, 1, color='C0', linewidth=1, width=0.01, length_includes_head=True,
         transform=mtransforms.Affine2D().translate(10*np.pi/180, 0) + ax.transData,
         head_width=0.08)
    
    ax.arrow(0, 0, 0, 1, color='C0', linewidth=1, width=0.01, length_includes_head=True,
         transform=mtransforms.Affine2D().translate(350*np.pi/180, 0) + ax.transData,
         head_width=0.08)
    
    ax.arrow(0, 0, 0, 1, color='C2', linewidth=1, width=0.01, length_includes_head=True,
         transform=mtransforms.Affine2D().translate(0, 0) + ax.transData,
         head_width=0.08)

    ax.set_ylim([0, 1.05])
    fig.tight_layout(pad=0.1)
    fig.subplots_adjust(left=1-fig.subplotpars.right)
    fig.savefig('/data/thesis/fig/circ_stats_intro/circ_mean')
