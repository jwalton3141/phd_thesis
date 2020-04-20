#! /usr/bin/env python

import sys
sys.path.insert(0, '..')
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sin, cos
from scipy.spatial import distance_matrix

from pretty import set_size


def main():
    # Setup
    cell_size = 1
    agents = 10
    radius = 0.15

    pos, angle, vel = make_data(cell_size, agents, radius)

    i = 1
    for time in range(16):
        fig, ax = make_fig_ax(cell_size, time)
        plot_agents(ax, pos, vel)
        interaction_radius(ax, pos, angle, radius, i)
        highlight_neighbours(ax, pos, radius, i)
        fig.savefig('vicsek_simulation_{}.pdf'.format(time), format='pdf')

        pos, angle, vel = update_agents(pos, angle, vel, cell_size, radius)


def make_data(cell_size, agents, radius):
    """Generate random data for plot."""
    # Positions
    pos = np.random.uniform(cell_size / 10,
                            cell_size / 10 * 9,
                            size=(2, agents))
    # Directions
    angle = np.random.uniform(-pi, pi, size=agents)

    # Corresponding velocities
    vel = np.vstack([cos(angle), sin(angle)])

    return pos, angle, vel


def make_fig_ax(cell_size, time):
    """Make figure and axes to plot on."""
    # Figure and axes to plot on
    fig, ax = plt.subplots(1, 1,
                           figsize=set_size(aspect='equal', fraction=0.5))

    # Wrangle with ticks, labels and limits
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim([0, cell_size])
    ax.set_ylim([0, cell_size])
    ax.text(cell_size / 10 * 8.75,
            cell_size / 10 * 9.5,
            '$t={}$'.format(time))
    fig.tight_layout()

    return fig, ax


def plot_agents(ax, pos, vel):
    """Plot the positions and directions of all the agents."""
    # Plot directions of motion
    ax.quiver(pos[0], pos[1],
              vel[0], vel[1],
              color='C0',
              scale_units='width',
              scale=7.5)


def interaction_radius(ax, pos, angle, radius, i):
    """Label agent i and visualise its interaction radius."""
    # Highlight agent i
    ax.text(pos[0, i] + 0.015,
            pos[1, i] + 0.015,
            '$i$')

    # Plot interaction radius
    theta = np.linspace(-pi, pi, num=100)
    ax.plot(pos[0, i] + radius * cos(theta),
            pos[1, i] + radius * sin(theta),
            c='C1',
            linestyle='--')

    # Add an arrow to indicate the size of the interaction radius
    label_r_angle = angle[i] + 3 * pi / 4
    label_r_vel = radius * np.array([cos(label_r_angle), 
                                     sin(label_r_angle)])

    hw = 0.02; hl = 0.02
    # Plot both ways to get double head
    ax.arrow(pos[0, i],
             pos[1, i],
             label_r_vel[0],
             label_r_vel[1],
             length_includes_head=True,
             head_width=hw, head_length=hl,
             color='k'
             )
    ax.arrow(pos[0, i] + label_r_vel[0],
             pos[1, i] + label_r_vel[1],
             -label_r_vel[0],
             -label_r_vel[1],
             length_includes_head=True,
             head_width=hw, head_length=hl,
             color='k'
             )
    # Annotate radius arrow a little away from the arrow
    ax.text(pos[0, i] + radius * cos(label_r_angle + pi / 10) / 2,
            pos[1, i] + radius * sin(label_r_angle + pi / 10) / 2,
            '$r$'
        )


def highlight_neighbours(ax, pos, radius, i):
    """Highlight the neighbours within agent i's interaction radius."""
    # Compute the distance between agent i and all its neighbours
    deltax = (pos[0, i] - pos[0]) ** 2
    deltay = (pos[1, i] - pos[1]) ** 2
    dist = (deltax + deltay) ** .5

    neighbours = dist <= radius
    # Highlight neighbours
    ax.scatter(pos[0, neighbours],
               pos[1, neighbours],
               c='C1', marker='x')
    # Highlight non-neighbours
    ax.scatter(pos[0, ~neighbours],
               pos[1, ~neighbours],
               c='C2', marker='x')


def update_agents(pos, angle, vel, cell_size, radius):
    # Update positions
    pos += 0.03 * vel
    # Wrap positions
    pos %= cell_size
    
    distances = distance_matrix(pos.T, pos.T)
    interact = distances <= radius
    # Update directions of motion according to vanilla Vicsek
    angle = (np.arctan2(np.dot(interact, sin(angle)),
                        np.dot(interact, cos(angle)))
             + np.random.uniform(-pi / 32, pi / 32, size=angle.size))
    # Wrap angles to -pi, pi
    angle = (angle + pi) % (2 * pi) - pi

    vel = np.vstack((cos(angle), sin(angle)))
    return pos, angle, vel


if __name__ == "__main__":
    main()
