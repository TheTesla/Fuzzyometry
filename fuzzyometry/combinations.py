
from numba import njit

@njit
def fz_chamfer(a, b, r):
    return r - (max(r-a, 0)**2 + max(r-b, 0)**2 )**0.5



