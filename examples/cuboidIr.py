#!/usr/bin/env python3

from numba import njit
from xyzcad import render

from fuzzyometry import bodies as fzbdy


@njit
def f(x, y, z):
    if max(abs(x), abs(y), abs(z)) > 20:
        return False

    # if fzbdy.cuboidIr((x,y,z),(10,20,30)) - 2 > 0:
    if fzbdy.fz_cuboid((x, y, z), (8, 5, 5)) + 0.5 < 0:
        return True
    return False


render.renderAndSave(f, "cuboid_ir.stl", 0.03)
