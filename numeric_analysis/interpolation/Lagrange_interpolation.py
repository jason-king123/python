#!D:/develop/Anaconda/python.exe
# -*- encoding: utf-8 -*-
'''
@filename     : Lagrange_interpolation.py
@description     :    
@time     : 2024/02/04/21
@author     : KING
'''

import numpy as np
import sympy as sp
import  matplotlib.pyplot as plt
from utils import interpolation_utils

class LarangeInterpolation:
    
    def __init__(self, x, y):
        self.x = np.asarray(x, dtype=float)
        self.y = np.asarray(y, dtype=float)
        if len(self.x) > 1 and len(self.x) == len(self.y):
            self.n = len(self.x)
        else:
            raise ValueError('Interpolated data (x,y) dimension does not match!')
        self.polynomial = None
        self.polynomial_coefficient = None
        self.coefficient_order = None
        self.x0 = None
        self.y0 = None
        self.fit_interpolation()

    def fit_interpolation(self):
        t = sp.Symbol('t')
        self.polynomial = 0.0
        for i in range(self.n):
            l_fun = self.y[i]
            for j in range(self.n):
                if j != i:
                    l_fun *= (t - self.x[j]) / (self.x[i] - self.x[j])
            self.polynomial += l_fun
        self.polynomial = sp.expand(self.polynomial)
        polynomial = sp.Poly(self.polynomial, t)
        self.polynomial_coefficient = polynomial.coeffs()
        self.coefficient_order = polynomial.monoms()

    def cal_interp_y0(self, x0):
        return interpolation_utils.cal_interp_y0(self.polynomial, x0)

    def show_interpolation(self, x0):
        interpolation_utils.show_interpolation(self.polynomial,self.x, self.y, x0)



