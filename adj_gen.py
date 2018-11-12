#!/usr/bin/env python3

"""adj_gen.py
Generate TSP adjacency matrix for polarization tomography.
2018 Radim Hošák <hosak.r@gmail.com>
Quantum Optics Lab Olomouc"""

from copy import deepcopy
import numpy as np

##################################
# Wave plate angle specification #
##################################

# The wave plate angles are stored in the ANGLES variable.

# The code below shows wave plate angle specification
# for a six-projection scheme (H, V, D, A, R, L),
# with a half-wave plate (HWP) and a quarter-wave plate (QWP).

ANGLES = np.array([[0, 0],
                   [45, 0],
                   [22.5, 0],
                   [-22.5, 0],
                   [0, 45],
                   [0, -45]])

# For a three-bases scheme (H/V, D/A, R/L),
# the ANGLES variable would look like this:

# ANGLES = np.array([[0, 0],
#                    [22.5, 0],
#                    [0, 45]])
