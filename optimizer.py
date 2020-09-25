import numpy as np
from numpy import linalg
import generator as gen

def gradient_descent(A, alpha, n, d):
    x = np.ones(d)

def pgd():
    pass

def gd_iter(x_t, alpha, grad):
    return x_t - alpha * grad

def gradient(A, x, b_t):  # ????
    return linalg.norm(A @ x - b_t) @ A