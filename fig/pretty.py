"""A module that helps produce publication-quality figures to be included in my thesis."""

import matplotlib as mpl
import os
if "DISPLAY" not in os.environ:
    mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os.path as path
import pickle


if path.isfile(path.join(mpl.__path__[0], 'mpl-data', 'stylelib', 'thesis.mplstyle')):
    plt.style.use('thesis')
else:
    plt.style.use('seaborn')


def set_size(width='thesis', fraction=1, aspect=None, subplots=[1, 1]):
    """
    Set aesthetic figure dimensions to avoid scaling in latex.

    Parameters
    ----------
    width: float or string, optional
            Width in pts or a predefined size, 'thesis', 'beamer', 'poster_col'
    fraction: float, optional
            Fraction of the textwidth which the figure is to occupy
    aspect: string, optional
            If aspect is equal ensure figure is square
    subplots: tuple, optional
            The subplots set when calling fig.subplots(a, b)

    Returns
    -------
    fig_dim: list
            Dimensions of figure in inches
    """
    # If using a pre-defined width
    if isinstance(width, str):
        if width == 'thesis':
            width_pt = 426.79135
    else:
        width_pt = width
    # Width of figure
    fig_width_pt = width_pt * fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    if aspect == 'equal':
        fig_dim = [fig_width_in, fig_width_in]
    else:
        fig_dim = [fig_width_in, fig_height_in]

    return fig_dim


def thousand_sep(label, pos):
    """
    Add latex thinspace to label to make long numbers easier to read.

    Parameters
    ----------
    label : string
        Label on plot.
    pos : TYPE
        DESCRIPTION.

    Returns
    -------
    label : string
        Label formatted to show thinspace for large number.

    """
    # Format label as integer
    label = int(label)
    # Personally only believe numbers >= 10,000 need a thinspace to aid readability
    if abs(label) >= 10000:
        label = ("{:,}".format(label)).replace(',', r'\,')
    return label


def savefig(fig, file, tight='tight', **kwargs):
    """
    Save figure in pdf format and as a pickle object.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        figure to save.
    file : string
        Name of file.
    tight: string or None, optional
        BBox of plot to save.
    **kwargs : dict
        Extra arguments to pass to fig.savefig().

    """
    # If file name passed already has .pdf extension strip it off
    if file[-4:] == ".pdf":
        file = file[:-4]

    fig.savefig(file + '.pdf', format='pdf', bbox_inches=tight, **kwargs)
    pickle.dump(fig, open(file + '.pkl', 'wb'))


def adjust_spacing(fig, subplots=(1, 1), fraction=1):
    """
    Adjust the spacing between axes and figure.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        figure instance.
    subplots: tuple, optional
            The subplots set when calling fig.subplots(a, b)
    fraction: float, optional
            Fraction of the textwidth which the figure is to occupy

    """
    # Adjust left and bottom padding based on axes layout
    fig.subplots_adjust(left=0.17,
                        bottom=0.14)
    # Padding for all plots
    fig.subplots_adjust(right=0.94,
                        wspace=0.3,
                        hspace=0.4,
                        top=0.985)


def rose_plot(ax, angles, bins=16, density=None, offset=0, lab_unit="degrees",
              start_zero=False, **param_dict):
    """
    Plot polar histogram of angles on ax. ax must have been created using
    subplot_kw=dict(projection='polar'). Angles are expected in radians.
    """
    # Wrap angles to [-pi, pi)
    angles = (angles + np.pi) % (2*np.pi) - np.pi

    # Set bins symetrically around zero
    if start_zero:
        # To have a bin edge at zero use an even number of bins
        if bins % 2:
            bins += 1
        bins = np.linspace(-np.pi, np.pi, num=bins+1)

    # Bin data and record counts
    count, bin = np.histogram(angles, bins=bins)

    # Compute width of each bin
    widths = np.diff(bin)

    # By default plot density (frequency potentially misleading)
    if density is None or density is True:
        # Area to assign each bin
        area = count / angles.size
        # Calculate corresponding bin radius
        radius = (area / np.pi)**.5
    else:
        radius = count

    # Plot data on ax
    ax.bar(bin[:-1], radius, zorder=1, align='edge', width=widths,
           edgecolor='C0', fill=False, linewidth=1)

    # Set the direction of the zero angle
    ax.set_theta_offset(offset)

    # Remove ylabels, they are mostly obstructive and not informative
    ax.set_yticks([])

    if lab_unit == "radians":
        tick_labels = [r'$0$',
                       r'$\pi/4$',
                       r'$\pi/2$',
                       r'$3\pi/4$',
                       r'$-\pi, \pi$',
                       r'$-3\pi/4$',
                       r'$-\pi/2$',
                       r'$-\pi/4$']
        ax.set_xticklabels(tick_labels)


