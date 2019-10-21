# -*- coding: utf-8 -*-
"""
    Pricing_aware_MEC_offloading.simulation
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Simulation for the Pricing_aware_MEC_offloading

    :copyright: (c) 2019 by Giorgos Mitsis.
    :license: MIT License, see LICENSE for more details.
"""

import numpy as np
import matplotlib.pyplot as plt

from helper_functions import *
from game_functions import *
from create_plots import *

def main(params):

    # b_old is only used to store the previous offloading decision to find convergence
    b,b_old = initialize(**params)

    converged = False
    while not converged:

        b = play_offloading_game(b, **params)

        # check if the game has reached a Nash equilibrium
        converged = game_converged(b, b_old, **params)

        b_old = b

    plot_utility_functions(b, **params)

    results = {
        "b": b,
            }

    return results
