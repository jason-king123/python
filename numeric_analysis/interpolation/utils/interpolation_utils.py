#!D:/develop/Anaconda/python.exe
# -*- encoding: utf-8 -*-
'''
@filename     : interpolation_utils.py
@description     :    
@time     : 2024/02/05/17
@author     : KING
'''



import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def cal_interp_y0(polynomial, x0):
        x_0 = np.asarray(x0, float)
        n = len(x_0)
        y_0 = np.zeros(n)
        t = polynomial.free_symbols.pop()
        for i in range(n):
            y_0[i] = polynomial.evalf(subs={t:x_0[i]})
        return y_0

def show_interpolation(polynomial, x, y, x0):
    plt.plot(x, y, 'ro', label='Interpolation base points')
    xi = np.linspace(min(x), max(x), 100)
    yi = cal_interp_y0(polynomial, xi)
    plt.plot(xi, yi, 'b--', label='Interpolation polynomial')
    if x0 is not None:
        plt.plot(x0, cal_interp_y0(polynomial, x0), 'g*', label='Interpolation points')
    plt.legend()
    plt.xlabel('x', fontdict={'fontsize': 12})
    plt.ylabel('y', fontdict={'fontsize': 12})
    plt.title('Lagrange Interpolation polynomial and values', fontdict={'fontsize':14})
    plt.show()
