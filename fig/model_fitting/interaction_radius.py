#! /usr/bin/env python3
""" Illustrate why we don't like the hard cut-off imposed by the interaction radius """

import matplotlib.pyplot as plt
import numpy as np
from plot.pretty_plot import set_size

if __name__ == "__main__":
    # Plot showing just in and just out case
    fig, ax = plt.subplots(1, 1, figsize=set_size(aspect='equal', fraction=0.45))
    ax.set_xticks([])
    ax.set_yticks([])
    x = np.linspace(0, 2*np.pi, num=100)
    ax.plot(np.sin(x), np.cos(x), ls='--')
    ax.scatter(0, 0, marker='x')
    ax.text(-0.1, 0.1, '$i$', ha='center', va='center', size=12)
    
    # Forwards head to annotate r
    ax.arrow(0, 0, np.cos(5*np.pi/4), np.sin(5*np.pi/4), color='C0', length_includes_head=True,
             width=0.005, head_width=0.04)
    # Backwards head (probably an easier way than this...)
    ax.arrow(np.cos(5*np.pi/4), np.sin(5*np.pi/4), -np.cos(5*np.pi/4), -np.sin(5*np.pi/4),
             color='C0', length_includes_head=True, width=0.005, head_width=0.04)
    ax.text(np.sin(5*np.pi/4)/2-0.05, np.cos(5*np.pi/4)/2+0.05, '$r$', ha='center', va='center',
            rotation=270-180/np.pi*5*np.pi/4)
    
    # Agent just inside r
    ax.scatter(0.9, 0.4, s=30, c='C1')
    ang = np.arctan2(0.4, 0.9)
    ax.arrow(0, 0, 0.9, 0.4, color='C1', length_includes_head=True, width=0.005, head_width=0.04)
    ax.arrow(0.9, 0.4, -0.9, -0.4, color='C1', length_includes_head=True, width=0.005,
             head_width=0.04)
    ax.text(0.45, 0.3, '$r - |\, \epsilon \,|$', ha='center', va='center', rotation=180/np.pi*ang)
    
    # Agent just outside r
    ax.scatter(0.9, -0.5, s=30, c='C2')
    ang = np.arctan2(-0.5, 0.9)
    ax.arrow(0, 0, 0.9, -0.5, color='C2', length_includes_head=True, width=0.005, head_width=0.04)
    ax.arrow(0.9, -0.5, -0.9, 0.5, color='C2', length_includes_head=True, width=0.005,
             head_width=0.04)
    ax.text(0.45, -0.35, '$r + |\, \epsilon \,|$', ha='center', va='center', rotation=180/np.pi*ang)
    fig.tight_layout(pad=0.1)
    fig.subplots_adjust(right=1-fig.subplotpars.left)
    fig.savefig('no_interact')

    # Plot showing close and far away case
    fig, ax = plt.subplots(1, 1, figsize=set_size(aspect='equal', fraction=0.45))
    ax.set_xticks([])
    ax.set_yticks([])
    x = np.linspace(0, 2*np.pi, num=100)
    ax.plot(np.sin(x), np.cos(x), ls='--')
    ax.scatter(0, 0, marker='x')
    ax.text(-0.1, 0.1, '$i$', ha='center', va='center', size=12)

    # Forwards head to annotate r
    ax.arrow(0, 0, np.cos(5*np.pi/4), np.sin(5*np.pi/4), color='C0', length_includes_head=True,
             width=0.005, head_width=0.04)
    # Backwards head (probably an easier way to do this...)
    ax.arrow(np.cos(5*np.pi/4), np.sin(5*np.pi/4), -np.cos(5*np.pi/4), -np.sin(5*np.pi/4),
             color='C0', length_includes_head=True, width=0.005, head_width=0.04)
    ax.text(np.sin(5*np.pi/4)/2-0.05, np.cos(5*np.pi/4)/2+0.05, '$r$', ha='center', va='center',
            rotation=270-180/np.pi*5*np.pi/4)

    # Agent just inside r
    ax.scatter(0.9, 0.4, s=30, c='C1')
    ang = np.arctan2(0.4, 0.9)
    ax.arrow(0, 0, 0.9, 0.4, color='C1', length_includes_head=True, width=0.005, head_width=0.04)
    ax.arrow(0.9, 0.4, -0.9, -0.4, color='C1', length_includes_head=True, width=0.005,
             head_width=0.04)
    ax.text(0.45, 0.3, '$r - |\, \epsilon \,|$', ha='center', va='center', rotation=180/np.pi*ang)

    # Agent very close to center
    s = 0.2
    ax.scatter(0.9*s, -0.5*s, s=30, c='C1')
    ang = np.arctan2(-0.5, 0.9)
    ax.arrow(0, 0, 0.9*s, -0.5*s, color='C1', length_includes_head=True, width=0.005, head_width=0.04)
    ax.arrow(0.9*s, -0.5*s, -0.9*s, 0.5*s, color='C1', length_includes_head=True, width=0.005,
             head_width=0.04)
    ax.text(0.05, -0.15, '$|\, \epsilon \,|$', ha='center', va='center', rotation=180/np.pi*ang)
    fig.tight_layout(pad=0.1)
    fig.subplots_adjust(right=1-fig.subplotpars.left)
    fig.savefig('interact')
