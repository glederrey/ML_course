# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """
    Least squares regression using normal equations
    :param y:
    :param tx:
    :return:
    """
    xx = np.dot(np.matrix.transpose(tx), tx)

    # handle non-inversable matrix case
    try:
        inv_xx = np.linalg.inv(xx)
    except:
        raise ValueError('Matrix X^TX is not invertible')

    w = np.matrix.dot(np.matrix.dot(inv_xx, np.matrix.transpose(tx)), y)
    loss = compute_loss(y, tx, w)

    return loss, w


def calculate_mse(e):
    """Calculate the mse for vector e."""
    return 1/2*np.mean(e**2)


def calculate_mae(e):
    """Calculate the mae for vector e."""
    return np.mean(np.abs(e))

def calculate_rmse(e):
    """Calculate the rmse for vector e"""
    return np.sqrt(2* calculate_mse(e))


def compute_loss(y, tx, w):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """
    e = y - tx.dot(w)
    # return calculate_mse(e)
    # return calculate_mae(e)
    return calculate_rmse(e)