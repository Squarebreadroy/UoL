# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:21:49 2024

@author: roy.fong
"""
import timeit

setup_iterative = """
from floyds_algorithm_iterative.floyds_iterative import floyd_iterative
graph = [[0, 7, sys.maxsize, 8],
[sys.maxsize, 0, 5, sys.maxsize],
[sys.maxsize, sys.maxsize, 0, 2],
[sys.maxsize, sys.maxsize, sys.maxsize, 0]]
"""

iterative_time = timeit.timeit(stmt="floyd_iterative(graph)",
                               setup=setup_iterative, number=20)
print(f"Iterative version time: {iterative_time} seconds")

setup_recursive = """
from floyds_algorithm_recursive.floyds_recursive import floyd_recursive
graph = [[0, 7, sys.maxsize, 8],
[sys.maxsize, 0, 5, sys.maxsize],
[sys.maxsize, sys.maxsize, 0, 2],
[sys.maxsize, sys.maxsize, sys.maxsize, 0]]
"""

recursive_time = timeit.timeit(stmt="floyd_recursive(graph)",
                               setup=setup_recursive, number=20)
print(f"Recursive version time: {recursive_time} seconds")
