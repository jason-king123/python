#!D:/develop/Anaconda/python.exe
# -*- encoding: utf-8 -*-
'''
@filename     : Lagrange_test.py
@description     :    
@time     : 2024/02/04/22
@author     : KING
@Version     : 1.0
'''

import numpy as np
from ..Lagrange_interpolation import LarangeInterpolation

if __name__ == '__main__':
    x = np.linspace(0, 2 * np.pi, 10)
    y = np.sin(x)
    lag_interp = LarangeInterpolation(x=x, y=y)
    lag_interp.fit_interpolation()
