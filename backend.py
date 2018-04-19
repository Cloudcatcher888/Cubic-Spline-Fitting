import scipy
from scipy.interpolate import CubicSpline, UnivariateSpline
import matplotlib.pyplot as plt
import numpy as np

def fit(arr, s=1):
    x = arr[:,0]
    y = arr[:,1]
    if arr.shape[1]==2:
        poly = UnivariateSpline(x, y, k=3, s=s)  # PPoly作为输出
    elif arr.shape[1]==3:
        w = arr[:,2]
        poly = UnivariateSpline(x, y, w, k=3, s=s)
    else:
        raise ValueError('Wrong input! Array do have 2 or 3 dim!')
    x_ = np.linspace(np.min(x),np.max(x),100)
    re = poly(x_)
    return x_, re