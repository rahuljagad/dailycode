'''
931. Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/
 - Solved using dynamic programming - 
'''
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        results = [[ 0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        # base case 
        for index in range(len(matrix[0])):
            results[0][index] = matrix[0][index]
        
        # iteration
        for index in range(1, len(matrix)):
            for inner_index in range(0, len(matrix[index])):
                left = results[index - 1][inner_index - 1] + matrix[index][inner_index] \
                    if inner_index > 0 else float("inf")
                upper = results[index - 1][inner_index] + matrix[index][inner_index]
                right = results[index - 1][inner_index + 1] + matrix[index][inner_index] \
                    if inner_index < len(matrix) - 1 else float("inf") 
                results[index][inner_index] = min(left, upper, right)
        
        return min(results[len(results) - 1])