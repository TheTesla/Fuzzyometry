import numpy as np
from numba import njit

from fuzzyometry import combinations as cmb


@njit
def evolvente(p, param):
    x, y, z = p[:3]
    z, m, alpha = param
    # z = 20
    # m = 1
    # alpha = 20 /180*np.pi
    d = m * z
    s = np.pi * m / 2
    d_b = d * np.cos(alpha)
    s_b = d_b * (s / d + np.tan(alpha) - alpha)
    p_b = np.pi * d_b / z
    e_b = p_b - s_b
    t = 2 * np.pi / z
    d_a = m * (z + 2)
    d_f = m * (z - 7 / 3)
    # print(f"z   = {z}")
    # print(f"m   = {m}")
    # print(f"d   = {d}")
    # print(f"s   = {s}")
    # print(f"d_b = {d_b}")
    # print(f"s_b = {s_b}")
    # print(f"p_b = {p_b}")
    # print(f"e_b = {e_b}")
    # print(f"t   = {t}")
    # print(f"d_f = {d_f}")

    R = max((x**2 + y**2) ** 0.5 / (d_b / 2), 1)
    Ra = (x**2 + y**2) ** 0.5 - d_a / 2

    T = (R**2 - 1) ** 0.5
    phi = T - np.arctan(T)
    phi2 = abs((np.arctan2(y, x)) % t - t / 2) - t / 2 * e_b / p_b
    Rf = (x**2 + y**2) ** 0.5 - d_f / 2

    return cmb.fz_or_chamfer(e_b / 2, d * cmb.fz_and_chamfer(0.1, phi - phi2, Ra), Rf)
    # return phi - phi2
