'''
https://leetcode.com/problems/squares-of-a-sorted-array
'''
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num * num for num in nums])
