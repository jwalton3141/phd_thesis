#! /usr/bin/env python3
""" Compare visualisation of circular data with a histograms and rose plots. """

import sys
sys.path.insert(0, '..')
import matplotlib.pyplot as plt
import numpy as np

from pretty import set_size, savefig, rose_plot


def main():
    """Produce histogram and polar histogram plots of random data."""
    # Random uniform data
    angles = np.random.uniform(-np.pi, np.pi, size=100)
    plot_angles(angles, 'uniform')

    # Random normal data
    angles = np.random.normal(loc=0, scale=1, size=10000)
    plot_angles(angles, 'normal')


def plot_angles(angles, save_name):
    """Plot and save histogram and polar histogram of angles."""
    fig, ax = make_fig_ax()
    plot_hist(fig, ax, angles)
    savefig(fig, '{}_hist'.format(save_name), tight=None)

    fig, ax = make_polar_fig_ax()
    plot_polar_hist(fig, ax, angles)
    savefig(fig, '{}_polar_hist'.format(save_name), tight=None)


def make_fig_ax():
    """Create empty figure and axes to plot regular histogram on."""
    fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.5))
    return fig, ax


def make_polar_fig_ax():
    """Create empty figure and axes to plot polar histogram on."""
    fig, ax = plt.subplots(1, 1,
                           figsize=set_size(fraction=0.45, aspect='equal'),
                           subplot_kw=dict(projection='polar'))
    return fig, ax


def plot_hist(fig, ax, angles):
    """Produce a histogram plot angles on ax."""
    ax.hist(angles, density=True, bins=16)

    ax.set_xlabel(r'$\theta$')
    ax.set_ylabel('density')

    ax.set_yticks([])
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])

    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', '$0$', r'$\pi/2$',r'$\pi$'])

    ax.set_xlim([-np.pi, np.pi])

    fig.tight_layout(pad=0.1)
    fig.subplots_adjust(right=1-fig.subplotpars.left)


def plot_polar_hist(fig, ax, angles):
    """Produce a polar histogram plot of angles on ax."""
    rose_plot(ax, angles, bins=16, start_zero=True, lab_unit='radians')
    fig.tight_layout(pad=0.1)
    fig.subplots_adjust(right=1-fig.subplotpars.left)


if __name__ == "__main__":
    main()

