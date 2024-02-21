# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:21:49 2024

@author: roy.fong
"""
import sys
import unittest
from floyds_algorithm_recursive.floyds_recursive import floyd_recursive
from floyds_algorithm_iterative.floyds_iterative import floyd_iterative

class TestFloydAlgorithm(unittest.TestCase):
    def test_floyd_recursive(self):
        graph = [
            [0, 7, sys.maxsize, 8],
            [sys.maxsize, 0, 5, sys.maxsize],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]
        expected_result = floyd_iterative(graph)
        with self.subTest():
            self.assertEqual(floyd_recursive(graph), expected_result)

        
        graph_with_negative = [
                    [0, -1, -2, 0],
                    [4, 0, 2, 4],
                    [2, 1, 0, 2],
                    [3, -1, 1, 0]
        ]
        expected_result = floyd_iterative(graph_with_negative)
        with self.subTest():
            self.assertEqual(floyd_recursive(graph_with_negative), expected_result)
   
        graph_with_more_vertices = [
                    [0, 4, 4, 3, sys.maxsize],
                    [3, 0, 7, 6, sys.maxsize],
                    [6, 3, 0, 2, sys.maxsize],
                    [4, 1, 1, 0, sys.maxsize],
                    [6, 3, 3, 2, 0]
        ]
        expected_result = floyd_iterative(graph_with_more_vertices)
        with self.subTest():
            self.assertEqual(floyd_recursive(graph_with_more_vertices), expected_result)
            
if __name__ == '__main__':
    unittest.main()
