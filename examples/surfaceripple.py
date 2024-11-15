#!/usr/bin/env python3

from xyzcad import render
from numba import njit
from fuzzyometry import bodies as fzbdy
from fuzzyometry import combinations as cmb

@njit
def f(x,y,z):
    if max(abs(x),abs(y),abs(z)) > 20:
        return False
    a = fzbdy.fz_cuboid((x,y,z),(16,6,6), 0.2)
    b = fzbdy.fz_circle((x%5-2.5,y%5-2.5), 0)

    if  cmb.fz_or_chamfer(0.3, a, b) < 0:
        return False
    return True


render.renderAndSave(f, 'surfaceripple.stl', 0.1)
