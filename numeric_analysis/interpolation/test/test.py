from Lagrange_interpolation import LarangeInterpolation
import numpy as np

if __name__ == '__main__':
    x = np.linspace(0, 2 * np.pi, 10, endpoint=True)
    y = np.sin(x)
    lag_interp = LarangeInterpolation(x=x, y=y)
    lag_interp.fit_interpolation()
    x0 = np.array([0.5*np.pi, np.pi/6])
    print(lag_interp.cal_interp_y0(x0))
    lag_interp.show_interpolation(x0)