#!/usr/bin/env python3

from xyzcad import render
from numba import njit
from fuzzyometry import bodies as fzbdy

@njit
def f(x,y,z):
    if fzbdy.fz_cuboid((x,y,z),(10,20,30)) - 5 < 0:
        return True
    return False


render.renderAndSave(f, 'cuboid_or.stl', 1)

