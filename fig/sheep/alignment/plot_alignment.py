#! /usr/bin/env python3

"""Plot the alignment of forward simulated flocks."""

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import pickle as pkl
import sys
sys.path.insert(0, '../..')

from pretty import set_size


labels = {'stan_gauss_dist_weighted_align.pkl': 'Gaussian',
          'stan_inv_dist_weighted_align.pkl': 'Power-law',
          'stan_null_align.pkl': 'Null',
          'stan_top_align.pkl': 'Topological',
          'mh_r_align.pkl': 'Vicsek'
          }

# Choose colours of models so that they match those in 'model_comparison.py'
colours = {'stan_gauss_dist_weighted_align.pkl': 'C2',
          'stan_inv_dist_weighted_align.pkl': 'C0',
          'stan_null_align.pkl': 'C3',
          'stan_top_align.pkl': 'C1',
          'mh_r_align.pkl': 'C4'
          }


def load_data():
    """Load the alignment data (precomputed elsewhere)."""
    with open('alignment.pkl', 'rb') as f:
        return pkl.load(f)


def plot_ensemble_seq(alignment, seq):
    """Plot ensemble alignment from forward simulations."""
    # Extract alignment
    seq_align = alignment[seq]
    # Number of observations in this sequence
    frames = seq_align['data'].size

    # Sort models by median alignment so the highest alignment is overlaid last
    median = {model: np.median(align) for model, align in seq_align.items()}
    median = sorted(median.items(), key=lambda x: x[1])
    # Don't include data in ordering (overlaid first)
    median = [med for med in median if 'data' not in med]

    fig, ax = plt.subplots(1, 1, figsize=set_size(fraction=0.55))
    # Loop over model fits
    for model, _ in median:
        # Alignment of model
        data = seq_align[model]
        # Plot the median alignment
        ax.plot(range(frames),
                np.median(data, axis=0),
                label=labels[model],
                c=colours[model])

        # Plot the lower and upper quartiles of the noise
        ax.fill_between(range(frames),
                        np.percentile(data, 25, axis=0),
                        np.percentile(data, 75, axis=0),
                        alpha=0.6,
                        color=colours[model])

    ax.set_xlim(0, frames-1)
    ax.set_ylabel('Alignment')
    ax.set_xlabel('$t$')

    fig.tight_layout(pad=0)
    fig.savefig('alignment_ensemble_{}.pdf'.format(seq))


def plot_sample_seq(alignment, seq):
    """Plot alignment from single forward simulations."""
    seq_align = alignment[seq]

    # Get the names of the fitted models
    models = list(set(seq_align.keys()) - set(['data']))

    # Get the number of frames in the sequence
    reps, frames = seq_align[models[0]].shape

    fig, ax = plt.subplots(1, 2, figsize=set_size(subplots=[1, 2]))
    # Number of individual forward simulations to show
    for i in range(2):
        # Chose random forward simulations to plot
        rand_seq_id = np.random.randint(0, reps)
    
        # Plot alignment of observed sequence
        if i:
            ax[i].plot(range(frames),
                   seq_align['data'],
                   c='k',
                   alpha=0.75,
                   label='Data',
                   zorder=-1)
        else:
            ax[i].plot(range(frames),
                   seq_align['data'],
                   c='k',
                   alpha=0.75,
                   zorder=-1)
        # Plot for each sequence
        for model in models:
            if i:
                ax[i].plot(range(frames),
                       seq_align[model][rand_seq_id],
                       c=colours[model],
                       label=labels[model])
            else:
                ax[i].plot(range(frames),
                       seq_align[model][rand_seq_id],
                       c=colours[model])

        #ax[i].set_ylim(0.968, 0.997)
        ax[i].set_xlim(0, frames-1)

        if not i:
            ax[i].set_ylabel('Alignment')
        else:
            ax[i].set_yticks([])

    fig.legend(ncol=6,
               handlelength=0.7,
               handletextpad=0.25,
               columnspacing=1.12,
               loc=9,
               bbox_to_anchor=(0.562, 1.075))
    fig.tight_layout(pad=0)
    fig.subplots_adjust(wspace=0.175, top=0.9)
    fig.savefig('alignment_single_{}.pdf'.format(seq))
 

def plot_seq(alignment, seq):
    """Make alignment plot seq."""

    # Plot single flocking events
    plot_sample_seq(alignment, seq)
    # Plot ensemble of flocking events
    plot_ensemble_seq(alignment, seq)


def main():
    """Plot alignments for all sequences."""
    # Load precomputed alignments
    alignment = load_data()

    # Loop over the fitted sequences
    #for seq in alignment.keys():
    for seq in [1, 2, 3]:
        plot_seq(alignment, seq)


if __name__ == "__main__":
    main()
