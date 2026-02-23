#!/usr/bin/env python3

import numpy as np
from numba import njit
from xyzcad import render

from fuzzyometry import combinations as cmb
from fuzzyometry import gears as fzgr


@njit
def f(p):
    x, y, z = p[:3]
    if z < 0:
        return False
    if z > 10:
        return False

    if fzgr.evolvente(p, (20, 1, 20 / 180 * np.pi)) > 0:
        return False
    return True


render.renderAndSave(f, "gear.stl", 0.3)
