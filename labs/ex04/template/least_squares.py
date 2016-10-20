# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns mse, and optimal weights
    # ***************************************************

    xx = np.dot(np.transpose(tx),tx)
    try:
        inv = np.linalg.inv(xx)
    except:
        raise ValueError("Matrix X^TX not invertible")
        
    xy = np.dot(np.transpose(tx),y)
    w_star = np.dot(inv, xy)
    
    return w_star 
