#!/usr/bin/env python3

"""Visualise hyperpriors."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma

import utils.read_write as rw


data_path = '/home/jack/Documents/sheep/data/sim/gauss_dist_weighted_hierarchy'
data = rw.load_pkl(data_path)

fig, ax = plt.subplots(2, 2)
ax = ax.reshape(4)


stan_data = {}
stan_data['m_Y_shape'] = 2
stan_data['m_Y_scale'] = 1 / 10
stan_data['v_Y_shape'] = 1.5
stan_data['v_Y_scale'] = 1 / 50
stan_data['m_X_shape'] = 65
stan_data['m_X_scale'] = 1
stan_data['v_X_shape'] = 10
stan_data['v_X_scale'] = 1 / 10


x = np.linspace(0, 0.5)
m_y = gamma.pdf(x, a=stan_data['m_Y_shape'],
                 scale=stan_data['m_Y_scale'])
ax[0].plot(x, m_y)
ax[0].set_xlabel(r'$m_Y$')
ax[0].vlines(data.m_Y, 0, m_y.max(), color='C1')


x = np.linspace(0, 0.1)
v_y = gamma.pdf(x,
                a=stan_data['v_Y_shape'],
                scale=stan_data['v_Y_scale'])
ax[1].plot(x, v_y)
ax[1].set_xlabel(r'$v_Y$')
ax[1].vlines(data.v_Y, 0, v_y.max(), color='C1')


x = np.linspace(10, 40)
m_x = gamma.pdf(x, a=stan_data['m_X_shape'],
                   scale=stan_data['m_X_scale'])
ax[2].plot(x, m_x)
ax[2].set_xlabel(r'$m_X$')
ax[2].vlines(data.m_X, 0, m_x.max(), color='C1')



x = np.linspace(0, 2)
v_x = gamma.pdf(x, a=stan_data['v_X_shape'],
                   scale=stan_data['v_X_scale'])
ax[3].plot(x, v_x)
ax[3].set_xlabel(r'$v_X$')
ax[3].vlines(data.v_X, 0, v_x.max(), color='C1')


fig.tight_layout(pad=0)