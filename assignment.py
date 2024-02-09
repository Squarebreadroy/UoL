# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:07:03 2024

@author: roy.fong
"""

import sys
 
# Constants
NO_PATH = sys.maxsize
 
# Example graph
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
 
def floyd_recursive(distance):
    """
    Recursively implements Floyd's algorithm to find the shortest paths between all pairs of vertices.
    This function initializes the recursive process.
 
    Args:
        distance (list): Adjacency matrix representing distances between nodes in the graph.
    """
    n = len(distance)
    def calculate_min_distance(start, end, intermediate):
        """
        Recursively calculates the minimum distance between two nodes considering an intermediate node.
 
        Args:
            start (int): The starting node index.
            end (int): The ending node index.
            intermediate (int): The index of the intermediate node through which the path may pass.
 
        Returns:
            int: The minimum distance between start and end nodes.
        """
        if intermediate == -1:
            return distance[start][end]
        without_intermediate = calculate_min_distance(start, end, intermediate - 1)
        with_intermediate = calculate_min_distance(start, intermediate, intermediate - 1) + calculate_min_distance(intermediate, end, intermediate - 1)
        return min(without_intermediate, with_intermediate)
 
    for i in range(n):
       for j in range(n):
           distance[i][j] = calculate_min_distance(i, j, len(distance)-1)
 
    return distance
 
# Running the algorithm
result = floyd_recursive(graph)
for row in result:
    print(row)
 
 
import unittest
 
class TestFloydAlgorithm(unittest.TestCase):
    def test_floyd_recursive(self):
        graph = [
            [0, 7, sys.maxsize, 8],
            [sys.maxsize, 0, 5, sys.maxsize],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]
        expected_result = [
            [0, 7, 12, 8],
            [sys.maxsize, 0, 5, 7],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]
        self.assertEqual(floyd_recursive(graph), expected_result)
 
if __name__ == '__main__':
    unittest.main()
