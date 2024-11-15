import subprocess

import pytest
from numba import njit

from fuzzyometry.bodies import fz_sphere


@njit
def sphere(x, y, z):
    return fz_sphere((x, y, z), 20)


def is_around(val1, val2, tol=0.001):
    return abs(val1 - val2) < tol


def test_fz_sphere():
    assert is_around(fz_sphere((0, 0, 0), 3), -3)
    assert is_around(fz_sphere((1, 0, 0), 3), -2)
    assert is_around(fz_sphere((0, 1, 0), 3), -2)
    assert is_around(fz_sphere((0, 0, 1), 3), -2)
    assert is_around(fz_sphere((1, 1, 0), 3), -1.586)
    assert is_around(fz_sphere((1, 0, 1), 3), -1.586)
    assert is_around(fz_sphere((0, 1, 1), 3), -1.586)
    assert is_around(sphere(1, 0, 0), -19)
