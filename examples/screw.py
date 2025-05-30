#!/usr/bin/env python3

from numba import njit
from xyzcad import render

from fuzzyometry import bodies as fzbdy
from fuzzyometry import combinations as cmb
from fuzzyometry import threads as fzthrd


@njit
def f(p):
    x, y, z = p[:3]
    k = 0.9
    s = 1.6
    a = fzbdy.fz_cuboid((x, y, z), (25, 25, 60), 0.2)
    #b = fzthrd.fz_thread((x, y, 1.01 * z / 6), 7.5, 4, s, 1.0)
    b = fzthrd.fz_thread((x, y, 1.02 * z / 6), 7.5, 4, s, 1.0)
    c = fzthrd.fz_thread((x, y, 1./2.), 3.6, 4, k, 1.0)
    if cmb.fz_and_chamfer(0.5, a, b, -c) > 0:
        return False

    return True


render.renderAndSave(f, "screw.stl", 0.1)
