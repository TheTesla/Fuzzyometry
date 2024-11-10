
from numba import njit


@njit
def fz_and_chamfer(r, *args):
    s = 0.0
    for a in args:
        s += max(r+a, 0)**2
    return r - s**0.5

@njit
def fz_or_chamfer(r, *args):
    return -fz_and_chamfer((-e for e in args), r)



