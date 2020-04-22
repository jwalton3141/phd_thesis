#! /usr/bin/env python

"""Produce visualisations of model schematics from a simulation of Vicsek."""

import sys
sys.path.insert(0, '..')
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sin, cos
from scipy.spatial import distance_matrix

from pretty import set_size


def make_data(cell_size, agents, radius):
    """Generate random positions and directions for initial conditions."""
    # Positions (cheat a bit and don't put agents too close to the edge)
    pos = np.random.uniform(cell_size / 10,
                            cell_size / 10 * 9,
                            size=(2, agents))
    # Directions
    angle = np.random.uniform(-pi, pi, size=agents)

    # Corresponding velocities
    vel = np.vstack([cos(angle), sin(angle)])

    return pos, angle, vel


def make_fig_ax(cell_size, time):
    """Visualisation of cell in which Vicsek simulation is occurring."""
    # Figure and axes to plot on
    fig, ax = plt.subplots(1, 1, figsize=set_size(aspect='equal',
                                                  fraction=0.5))

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
    """Plot the positions and directions of all the agents on ax."""
    # Plot directions of motion
    ax.quiver(pos[0], pos[1],
              vel[0], vel[1],
              color='C0',
              scale_units='width',
              scale=7.5)


def interaction_radius(ax, pos, angle, radius, i):
    """Annotate agent i and visualise its interaction radius."""
    # Annotate agent i
    ax.text(pos[0, i] + 0.015,
            pos[1, i] + 0.015,
            '$i$')

    # Plot interaction radius
    theta = np.linspace(-pi, pi, num=100)
    # Interaction zone is a circle or radius r centred at pos[:, i]
    ax.plot(pos[0, i] + radius * cos(theta),
            pos[1, i] + radius * sin(theta),
            c='C1',
            linestyle='--')

    # Add an arrow to indicate the size of the interaction radius

    # Make the arrow point 3pi/4 radians away from agent i's direction
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
    """Highlight neighbours within agent i's interaction radius."""
    # Compute the distance between agent i and all its neighbours
    deltax = (pos[0, i] - pos[0]) ** 2
    deltay = (pos[1, i] - pos[1]) ** 2
    dist = (deltax + deltay) ** .5

    # Boolean array detailing agents within agent i's interaction zone
    neighbours = dist <= radius

    # Highlight agents within interaction zone with green markers
    ax.scatter(pos[0, neighbours],
               pos[1, neighbours],
               c='C1', marker='x')

    # Highlight agents outside interaction zone with red markers
    ax.scatter(pos[0, ~neighbours],
               pos[1, ~neighbours],
               c='C2', marker='x')


def update_agents(pos, angle, vel, cell_size, radius):
    """Simulate the vicsek model forward a step."""
    # Update positions
    pos += 0.03 * vel

    # Wrap positions (periodic boundary conditions)
    pos %= cell_size

    # Compute the pairwise distances between individuals
    distances = distance_matrix(pos.T, pos.T)

    # Boolean array indicating which agents interact
    interact = distances <= radius

    # Update directions of motion according to vanilla Vicsek
    angle = (np.arctan2(np.dot(interact, sin(angle)),
                        np.dot(interact, cos(angle)))
             + np.random.uniform(-pi / 32, pi / 32, size=angle.size))

    # Wrap angles to -pi, pi
    angle = (angle + pi) % (2 * pi) - pi

    # Convert new direction of motion to a velocity
    vel = np.vstack((cos(angle), sin(angle)))

    return pos, angle, vel


def produce_schematic(pos, angle, vel, radius, cell_size, i, t):
    """
    Produce visualisation of data, illustrating the interaction zone of
    agent i, and highlighting agents included and excluded from this zone.
    """
    # Figure and axes visualising simulation cell
    fig, ax = make_fig_ax(cell_size, t)

    # Quiver plot the positions and velocities of all agents
    plot_agents(ax, pos, vel)

    # Overlay the interaction zone of agent i
    interaction_radius(ax, pos, angle, radius, i)

    # Colour code agents within and outside agent i's interaction zone
    highlight_neighbours(ax, pos, radius, i)

    return fig, ax


def main():
    """The bit to run, duh"""
    # Simulation setup
    cell_size = 1
    agents = 10
    radius = 0.15

    # Number of steps to simulate
    T = 16
    # ID of agent to highlight
    i = 1

    # Initial conditions
    pos, angle, vel = make_data(cell_size, agents, radius)

    # Simulate and produce schematics for Vicsek over T times
    for t in range(T):
        fig, ax = produce_schematic(pos, angle, vel, radius, cell_size, i, t)

        # Save schematic
        fig.savefig('vicsek_simulation_{}.pdf'.format(t), format='pdf')

        # Update positions, directions and velocities according to Vicsek
        pos, angle, vel = update_agents(pos, angle, vel, cell_size, radius)


if __name__ == "__main__":
    main()
