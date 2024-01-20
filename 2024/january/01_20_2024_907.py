'''
907. Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/
Learnt from watching this NeetCode Video:
https://www.youtube.com/watch?v=aX1F2-DrBkQ
'''
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        total_sum = 0
        arr = [float("-inf")] + arr + [float("-inf")]
        stack = []
        for index_i, value in enumerate(arr):
            while stack and value < stack[-1][1]:
                index_j, value_m = stack.pop()
                left = index_j - stack[-1][0] if stack else index_j + 1
                right = index_i - index_j
                total_sum = (total_sum + value_m * left * right) % MOD
            stack.append((index_i, value))
        return total_sum