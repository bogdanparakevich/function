import numpy as np

def ds_generation(first_lim_x1, second_lim_x1, step_x1, first_lim_x2, second_lim_x2, step_x2):
    x1 = np.arange(first_lim_x1, second_lim_x1, step_x1)
    x2 = np.arange(first_lim_x2, second_lim_x2, step_x2)
    x = np.array(np.meshgrid(x1,x2)).T.reshape(-1,2)
    x1_new = x[:, 0]
    x2_new = x[:, 1]
    x_new = np.array([2 * x1_new, x2_new]).T
    y = np.max(x_new, axis=1)
    return x_new, y