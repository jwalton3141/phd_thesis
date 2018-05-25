#! /usr/bin/env python3
""" Script to generate plots which compare different angle measuring conventions. """

from plot.pretty_plot import set_size
import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.4, subplot=[1, 1], aspect='equal'),
                           subplot_kw=dict(projection='polar'))
    # Turn of radial grid
    ax.yaxis.grid(False)
    # Remove 'radius' marks
    ax.set_yticks([])

    lab = [r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$-\pi, \pi$',
           r'$-3\pi/4$', r'$-\pi/2$', r'$-\pi/4$']
    ax.set_xticklabels(lab)
    fig.savefig('/data/thesis/fig/circ_stats_intro/radian_axes', pad_inches=0.05)
    
    fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.4, subplot=[1, 1], aspect='equal'),
                       subplot_kw=dict(projection='polar'))
    ax.yaxis.grid(False)
    ax.set_yticks([])

    # Hack hack hack
    plt.pause(1)
    tick_labels = ax.get_xticklabels()
    # Change 0 label to show 0 AND 360
    tick_labels[0].set_text('$360^\\circ, 0^\\circ$')
    ax.set_xticklabels(tick_labels)

    fig.savefig('/data/thesis/fig/circ_stats_intro/degree_axes', pad_inches=0.05)