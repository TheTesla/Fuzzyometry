#!/usr/bin/env python3

from numba import njit
from xyzcad import render

from fuzzyometry import threads as fzthrd


@njit
def f(x, y, z):
    if max(abs(x), abs(y), abs(z)) > 20:
        return False

    if fzthrd.fz_thread((x,y,z)) > 0:
        return False
    return True


render.renderAndSave(f, "screw.stl", 0.1)
