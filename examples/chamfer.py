#!/usr/bin/env python3

from numba import njit
from xyzcad import render

from fuzzyometry import bodies as fzbdy
from fuzzyometry import combinations as cmb


@njit
def f(x, y, z):
    if max(abs(x), abs(y), abs(z)) > 20:
        return False
    a = fzbdy.fz_cuboid((x, y, z), (16, 6, 6), 0.2)
    # b = fzbdy.fz_cuboid((x,y,z),(2,16,2), 0.2)
    b = fzbdy.fz_circle((x, y), 2)
    c = fzbdy.fz_sphere((x - 5, y, z - 2), 2)

    if cmb.fz_and_chamfer(0.3, a, -b, -c) < 0:
        return False
    return True


render.renderAndSave(f, "chamfer.stl", 0.1)
