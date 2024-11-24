from numba import njit
import numpy as np



@njit
def fz_thread_profile(pnt, a=1.0):
    x, y = pnt[:2]
    p = a/(-0.5*np.sin(x) +0.0005 -0.001*np.sign(np.sin(x)))
    q = y/(np.sin(x) +0.0005 +0.001*np.sign(np.sin(x))) - 1
    return -p/2 - np.sign(np.sin(x))*(max(0,(p/2)**2 - q))**0.5

@njit
def fz_thread(pnt, radius, a=1.0):
    x, y, z = pnt
    ang = -np.atan2(y, x)
    r = (x**2 + y**2)**0.5
    return fz_thread_profile((z+ang, r-radius), a)


