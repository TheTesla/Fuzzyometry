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
    k = 2
    s = 2
    a = 0.2*fzbdy.fz_cuboid((x, y, z), (25, 25, 30), 0.2)
    b = fzthrd.fz_thread((x, y, z / 4), 5, 4, s, 1.0)
    c = fzthrd.fz_thread((x, y, 1./2.), 1.0, 4, k, 1.0)
    if cmb.fz_and_chamfer(1., a, b, -c) > 0:
        return False

    return True


render.renderAndSave(f, "screw.stl", 0.1)
