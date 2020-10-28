#!/usr/bin/env python3

"""
Produce plots which illustrate chains which are mixing well,
and chains which are mixing poorly.
"""

import sys
sys.path.insert(0, '..')
import numpy as np
import matplotlib.pyplot as plt

from pretty import set_size, savefig


class AR():
    """Class to represent an autoregressive model."""

    def __init__(self, alpha, beta, sigma):
        """
        Initialise class instance.
        Parameters
        ----------
        alpha : float
            Additive constant.
        beta : array-like, float.
            Parameters of the model.
        sigma : float
            Standard deviation of the noise distribution.
        """
        self.alpha = alpha
        self.beta = beta
        self.lag = self.beta.size
        self.sigma = sigma
        self.data = None

    def simulate(self, n=200):
        """
        Simulate the model for n time steps.
        Parameters
        ----------
        n : int, optional
            The number of data points to generate. The default is 200.
        """
        self.data = np.zeros(n)

        # Generate noise for sequence
        noise = np.random.normal(scale=self.sigma, size=n)

        # Generate initial data points
        self.data[:self.lag] = self.alpha + noise[:self.lag]

        # Simulate AR(K) process
        for t in range(self.lag, n):
            self.data[t] = (self.alpha
                           + np.sum(self.beta * self.data[t-self.lag:t][::-1])
                           + noise[t])

    def plot(self, filename=False, colour='C0', label_y = True):
        """
        Plot the time series.
        Parameters
        ----------
        filename : string, optional
            The name to use when saving the plot to file. By default the plot
            is not saved.
        """
        fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.5))

        ax.plot(np.r_[:self.data.size], self.data, color=colour)

        ax.set_xlabel('')
        ax.set_xlim(0, self.data.size)
        ax.set_xticks([0, self.data.size // 2, self.data.size])
        ax.set_xticklabels(['$0$', r'{\normalsize iteration}','$n$'])
        ax.set_yticks([])
        if label_y:
            ax.set_ylabel(r'$\theta$')

        if filename:
            filename += '.pdf' * (filename[-4:] != '.pdf')
            fig.savefig(filename, format='pdf', bbox_inches='tight')

    def save(self, filename=None):
        """
        Save this object instance.
        Parameters
        ----------
        filename : string, optional
            The name to use when saving this instance to file. If a file name
            isn't given, the instance well be saved as ARN.pkl where N is the
            order of the model.
        """
        if not filename:
            filename = 'AR{}'.format(self.lag)

        filename += '.pkl' * (filename[-4:] != '.pkl')
        file_path = path.join(path.dirname(path.realpath(__file__)),
                              'data',
                              filename)
        with open(file_path, "wb") as f:
            pickle.dump(self, f, protocol=-1)


def good_mixing(iters):
    """
    Produce a plot which illustrates two chains which have large between-chain
    variance, but small within-chain variance.
    """
    alpha = 0
    beta = np.array([0])
    sigma = 0.00001
    AR1 = AR(alpha, beta, sigma)
    AR1.simulate(n=iters)
    AR1.plot(filename='good_mixing.pdf')


def poor_mixing(iters):
    """
    Produce a plot which illustrates two chains which have large within-chain
    variance, but small between-chain variance.
    """
    alpha = 0
    beta = np.array([0.96])
    sigma = 0.01
    AR1 = AR(alpha, beta, sigma)
    AR1.simulate(n=iters)
    AR1.data += np.linspace(0, 0.125, num=iters)
    AR1.plot(filename='poor_mixing.pdf', colour='C2', label_y=False)


def main():
    iters = 1000
    good_mixing(iters)
    poor_mixing(iters)


if __name__ == "__main__":
    main()

