# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
    
    n_x = len(x)
    mat = np.zeros((n_x, degree+1))
        
    for i in range(n_x):
        for j in range(degree+1):
            mat[i][j] = x[i]**j
            
    return mat               