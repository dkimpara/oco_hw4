import numpy as np
from numpy import linalg


def generate_A(n,d):
    pass


def generate_bt(A, sigma, n, d):
    '''generator for b_t'''
    x = xstar(sigma, d)
    while True:
        w = np.random.normal(0, 10 ** (-3), n)
        yield np.matmul(A, next(x)) + w


def xstar(sigma, d):
    '''generator for x_t^*'''
    x = np.zeros(d)
    while True:
        x += sigma * sample_n_sphere_surface(d)
        yield x


def sample_n_sphere_surface(ndim, norm_p=2):
    """sample random vector from S^n-1 with norm_p"""

    vec = np.random.randn(ndim)
    vec = vec / linalg.norm(vec, norm_p)  # create random vector with norm 1
    return vec