# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 17:19:02 2024

@author: roy.fong
"""

import sys

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])

def floyd(distance:list)->list:
    """
    Floyd's algorithm with recurrsion, Time complexity: O(n**2)
    """
    for start_node in range(len(graph[0])):
        for end_node in range(len(graph[0])):
        #return all possible paths and find the minimum
            distance[start_node][end_node] = calculate_dist(start_node, end_node, 3)
        #Any value that have sys.maxsize has no path
    print (distance)
    
def calculate_dist(start:int,end:int,step:int)->int:
    """
    Recurrsion function for calculate the minimum distance.
    
    Args:
        start (int): start_node
        end (int): end_node 
        step (int): flexiability of intermediate_node (e.g.: 3 means 0,1,2,3 nodes can be the intermediate_node)
    
    Returns:
        int: Minimum distance from 
    """    
    if step==-1:
        return graph[start][end]
    return min(calculate_dist(start, end, step-1),calculate_dist(start, step, step-1)+calculate_dist(step, end, step-1))

floyd(graph)

