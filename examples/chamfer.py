#!/usr/bin/env python3

from xyzcad import render
from numba import njit
from fuzzyometry import bodies as fzbdy
from fuzzyometry import combinations as cmb

@njit
def f(x,y,z):
    if max(abs(x),abs(y),abs(z)) > 20:
        return False
    a = fzbdy.fz_cuboid((x,y,z),(16,6,6), 0.1)
    b = fzbdy.fz_cuboid((x,y,z),(2,16,2), 0.11)

    if  cmb.fz_and_chamfer(0.5, a, -b) < 0:
        return False
    return True


render.renderAndSave(f, 'chamfer.stl', 0.1)
