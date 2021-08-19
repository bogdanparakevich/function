import numpy as np

def ds_generation(a1, b1, c1, a2, b2, c2):
    x1 = np.arange(a1, b1, c1)
    x2 = np.arange(a2, b2, c2)
    x = np.array(np.meshgrid(x1,x2)).T.reshape(-1,2)
    x1_new = x[:, 0]
    x2_new = x[:, 1]
    x_new = np.array([2 * x1_new, x2_new]).T
    y = np.max(x_new, axis=1)
    return x_new, y