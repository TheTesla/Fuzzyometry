#!/usr/bin/env python3

from numba import njit
from xyzcad import render

from fuzzyometry import bodies as fzbdy
from fuzzyometry import combinations as cmb
from fuzzyometry import threads as fzthrd


@njit
def f(x, y, z):
    if max(abs(x), abs(y), abs(z)) > 20:
        return False
    a = fzbdy.fz_cuboid((x, y, z), (25, 25, 30), 0.2)
    b = fzthrd.fz_thread((x, y, z / 6), 10, 4, 1.0)
    if cmb.fz_and_chamfer(1.5, a, b) > 0:
        return False

    return True


render.renderAndSave(f, "screw.stl", 0.1)
