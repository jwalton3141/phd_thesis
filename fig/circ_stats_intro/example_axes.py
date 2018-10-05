#! /usr/bin/env python3
""" Script to generate plots which compare different angle measuring conventions. """

from plot.pretty import set_size
import matplotlib.pyplot as plt

if __name__ == "__main__":    
    fig1, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.5, aspect='equal'),
                       subplot_kw=dict(projection='polar'))
    ax.yaxis.grid(False)
    ax.set_yticks([])
    # Hack hack hack
    plt.pause(1)
    tick_labels = ax.get_xticklabels()
    # Change 0 label to show 0 AND 360
    tick_labels[0].set_text('$360^\\circ, 0^\\circ$')
    ax.set_xticklabels(tick_labels)
    fig1.tight_layout(pad=0.1)
    # Pad left and right side equally so subcpation appears in centre of plot
    fig1.subplots_adjust(left=1-fig1.subplotpars.right)
    fig1.savefig('/data/thesis/fig/circ_stats_intro/degree_axes')

    fig2, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.5, aspect='equal'),
                           subplot_kw=dict(projection='polar'))
    # Turn of radial grid
    ax.yaxis.grid(False)
    # Remove 'radius' marks
    ax.set_yticks([])

    lab = [r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$-\pi, \pi$',
           r'$-3\pi/4$', r'$-\pi/2$', r'$-\pi/4$']
    ax.set_xticklabels(lab)
    fig2.tight_layout(pad=0.1)
    # Pad as in figure 1, otherwise because labels are different, different sized circles produced
    fig2.subplots_adjust(right=fig1.subplotpars.right, left=fig1.subplotpars.left)
    fig2.savefig('/data/thesis/fig/circ_stats_intro/radian_axes')