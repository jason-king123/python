import numpy as np
import matplotlib.pyplot as plt
from Lagrange_interpolation import LarangeInterpolation

def runge(x):
    return 1 / (1 + x**2)

if __name__ == '__main__':
    plt.figure(figsize=(8, 6))
    xi = np.linspace(-5, 5, 100, endpoint=True)
    for n in range(3, 12, 2):
        x = np.linspace(-5, 5, n, endpoint=True)
        y = runge(x)
        lag_interp = LarangeInterpolation(x, y)
        yi = lag_interp.cal_interp_y0(xi)
        plt.plot(xi, yi, lw=0.7, label='n = %d' % (n - 1))

    plt.plot(xi, runge(xi), 'k-', label=r'$\frac{1}{1+x^{2}}$')
    plt.xlabel("x",fontdict={"fontsize":12})
    plt.ylabel("y",fontdict={"fontsize":12})
    plt.title("Runge phenomenon of lagrange interpolation of different orders",fontdict={"fontsize":14})
    plt.legend()
    plt.show()