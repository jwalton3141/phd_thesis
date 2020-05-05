#!/usr/bin/env python3

"""Produce plots showing interaction weighting kernel for metric models."""

import sys
sys.path.insert(0, '..')
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

from pretty import set_size, savefig


def vicsek_n_noise():
    """Plot prior beliefs for the parameters r, sigma_Y and nu."""
    figsize = set_size()
    # Ignore my over-engineered plot dimension considerations
    figsize[1] = 1.7

    # Make plot
    fig, ax = plt.subplots(1, 3, figsize=figsize)

    # Only label the y-axis of the left-most axis
    [ax[i].set_ylabel('') for i in [1, 2]]
    ax[0].set_ylabel('density')

    # Label x-axis of all axes
    labels = ['$r$', r'$\sigma_Y$', r'$\nu$']
    [ax[i].set_xlabel(lab) for i, lab in enumerate(labels)]

    # Prior beliefs about r
    lower, upper = 30, 70
    x = np.linspace(lower, upper, num=100)
    ax[0].plot(x, gamma.pdf(x, a=50, scale=1), c='C2')
    ax[0].set_xlim(lower, upper)

    # Prior beliefs about sigma_Y
    lower, upper = 0, 0.1
    x = np.linspace(lower, upper, num=100)
    ax[1].plot(x, gamma.pdf(x, a=2, scale=1 / 100), c='C2')
    ax[1].set_xlim(lower, upper)

    # Prior beliefs about nu
    lower, upper = 0, 75
    x = np.linspace(lower, upper, num=100)
    ax[2].plot(x, gamma.pdf(x, a=2, scale=1 / 0.1), c='C2')
    ax[2].set_xlim(lower, upper)

    fig.tight_layout(pad=0)
    fig.savefig('vicsek_priors.pdf')


def gauss_power():
    """Plot prior beliefs for the parameters alpha and sigma_X."""
    # Figure and axes to plot on
    fig, ax = plt.subplots(1, 2, figsize=set_size(subplots=(1, 2)))

    # Only label y-axis of leftmost axis
    ax[0].set_ylabel('density')
    ax[1].set_ylabel('')

    # Label x-axis of axes
    labels = [r'$\alpha$', r'$\sigma_X$']
    [ax[i].set_xlabel(lab) for i, lab in enumerate(labels)]

    # Prior beliefs about alpha
    lower, upper = 0, 15
    x = np.linspace(lower, upper, num=100)
    ax[0].plot(x, gamma.pdf(x, a=2, scale=2), c='C2')
    ax[0].set_xlim(lower, upper)

    # Prior beliefs about sigma_X
    lower, upper = 0, 60
    x = np.linspace(lower, upper, num=100)
    ax[1].plot(x, gamma.pdf(x, a=5, scale=5), c='C2')
    ax[1].set_xlim(lower, upper)

    fig.tight_layout(pad=0.25)
    fig.savefig('gauss_power_priors.pdf')


def main():
    #vicsek_n_noise()
    gauss_power()


if __name__ == "__main__":
    main()
