#! /usr/bin/env python3
""" Compare visualisation of circular data with a histograms and rose plots. """

import matplotlib.pyplot as plt
import numpy as np
from plot.pretty_plot import set_size, savefig
import plot.data as dplt

if __name__ == "__main__":
    # Generate random uniform data
    angles = np.random.uniform(-np.pi, np.pi, size=100)

    # Plot data as traditional histogram
    fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.49))
    ax.hist(angles, density=True, bins=16)
    ax.set_xlabel(r'$\theta$')
    ax.set_ylabel('density')
    ax.set_yticks([])
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', '$0$', r'$\pi/2$',r'$\pi$'])
    ax.set_xlim([-np.pi, np.pi])
#    savefig('/data/thesis/fig/circ_stats_intro/', 'unif_angle_hist')

    # Plot data on rose plot
    fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.40, aspect='equal'),
                           subplot_kw=dict(projection='polar'))
    dplt.rose_plot(ax, angles, bins=16)
    savefig('/data/thesis/fig/circ_stats_intro/', 'unif_angle_rose')

    # Generate random normal data
    angles = np.random.normal(loc=0, scale=1, size=10000)
    fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.49))
    ax.hist(angles, density=True, bins=20)
    ax.set_xlabel(r'$\theta$')
    ax.set_ylabel('density')
    ax.set_yticks([])
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', '$0$', r'$\pi/2$',r'$\pi$'])
    ax.set_xlim([-np.pi, np.pi])
    savefig('/data/thesis/fig/circ_stats_intro/', 'norm_angle_hist')

    # Plot same data on a rose plot
    fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.40, aspect='equal'),
                           subplot_kw=dict(projection='polar'))
    dplt.rose_plot(ax, angles, bins=20)
#    savefig('/data/thesis/fig/circ_stats_intro/', 'norm_angle_rose')