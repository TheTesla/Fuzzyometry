#!/usr/bin/env python3

from xyzcad import render
from numba import njit
from fuzzyometry import bodies as fzbdy

@njit
def f(x,y,z):
    if fzbdy.cuboidOr((x,y,z),(10,20,30)) - 5 < 0:
        return True
    return False


render.renderAndSave(f, 'cuboidOr.stl', 1)

