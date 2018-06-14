#!/usr/bin/env python3
""" Make a streamline plot which shows that highlighting can be useful """

import matplotlib.pyplot as plt
from plot.pretty_plot import set_size
import tools
import numpy as np

# Lifted these functions straight from streamline_plots.py and altered

def set_limits(ax, data):
    """ Set x and y limits of plots such that all data will be in the axes. """
    # Extract data which is observed
    observed = data[np.where(data[:, :, 4] == -1)]
    # Min and max x coordinates of observed data
    min_x, max_x = observed[:, 0].min(), observed[:, 0].max()
    # Min and max y coodinates of observed data
    min_y, max_y = observed[:, 1].min(), observed[:, 1].max()
    ax.set_xlim([min_x, max_x])
    ax.set_ylim([min_y, max_y])
    return ax

def plot_sequence(ax, data, highlight=[]):
    """ Plot trajectories in data[file] and save """
    # List of observed agents
    agents = np.unique(np.where(data[:, :, 4] == -1)[1])
    # If no agents highlighted, plot all trajectories darker
    if len(highlight) == 0:
        shade = 0.3
    else:
        shade = 0.15
    for agent in agents:
        # Frames where agent is observed
        frames = np.where(data[:, agent, 4] == -1)[0]

        # Use darker line for highlighted agents
        if agent in highlight:
            ax.plot(data[frames, agent, 0], data[frames, agent, 1], c='C0')
            ax.scatter(data[frames[0], agent, 0], data[frames[0], agent, 1], c='C1', s=20)
            ax.scatter(data[frames[-1], agent, 0], data[frames[-1], agent, 1], c='C2', s=20)
        # Use a lighter line for agents which aren't highlighted
        else:
            ax.plot(data[frames, agent, 0], data[frames, agent, 1], c='C0', alpha=shade)
            ax.scatter(data[frames[0], agent, 0], data[frames[0], agent, 1],
                       c='C1', s=20, alpha=shade)
            ax.scatter(data[frames[-1], agent, 0], data[frames[-1], agent, 1],
                       c='C2', s=20, alpha=shade)

    ax.set_aspect('equal')
    ax.set_axis_off()

if __name__ == "__main__":
    plt.style.use('thesis')
    data = tools.load_obj('/data/surf_scoter/infer/inputs/data')
    
    fig, ax = plt.subplots(1, 1, figsize=set_size(aspect='equal', fraction=0.5))
    plot_sequence(ax, data['sequence05'], highlight=[1, 20, 50, 63, 1])
    fig.savefig('/data/thesis/fig/model_fitting/streamline_plots/sequence05_highlight.pdf', format='pdf', bbox_inches='tight')
   