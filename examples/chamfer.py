#!/usr/bin/env python3

from xyzcad import render
from numba import njit
from fuzzyometry import bodies as fzbdy
from fuzzyometry import combinations as cmb

@njit
def f(x,y,z):
    if max(abs(x),abs(y),abs(z)) > 20:
        return False
    a = -(fzbdy.fz_cuboid((x,y,z),(8,3,3)) -1)
    b = fzbdy.fz_cuboid((x,y,z),(1,8,1)) -1

    if  cmb.fz_chamfer(a, b, 1) < 0:
        return False
    return True


render.renderAndSave(f, 'chamfer.stl', 0.1)
