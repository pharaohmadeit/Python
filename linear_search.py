# coding: utf-8
"""Sorting a numpy array object with linear search algorithm."""
def linear_search(data, search_key):
    for index, value in enumerate(data):
        if value == search_key:
            return index
    return -1
    
import numpy as np
np.random.seed(11)
values = np.random.randint(10, 91, 10)
values
linear_search(values, 23)
linear_search(values, 61)
linear_search(values, 34)
