# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""

import numpy as np

def split_data(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    
    n = len(x)
    if len(y) != n:
        raise ValueError("Vector x and y have a different size")
        
    n_train = int(ratio*n)
    train_ind = np.random.choice(n, n_train, replace=False)
        
    index = np.arange(n)
    
    mask = np.in1d(index, train_ind)
    
    test_ind = np.random.permutation(index[~mask])
    
    x_train = x[train_ind]
    y_train = y[train_ind]
    
    x_test = x[test_ind]
    y_test = y[test_ind]
    
    return x_train, y_train, x_test, y_test
    
def split_data_2(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    # ***************************************************
    
    index = np.arange(x.shape[0])
    shuffled_index = np.random.permutation(index)
   
    n_train = np.int(x.shape[0] * ratio)
    n_test = x.shape[0] - n_train
   
    shuffled_index_train = shuffled_index[: n_train]
    shuffled_index_test = shuffled_index[n_train : x.shape[0]]
   
    x_train = x[shuffled_index_train]
    y_train = y[shuffled_index_train]
    x_test = x[shuffled_index_test]
    y_test = y[shuffled_index_test]
   
    return x_train, y_train, x_test, y_test
