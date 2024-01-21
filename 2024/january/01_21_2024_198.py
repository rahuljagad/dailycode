'''
198. House Robber
https://leetcode.com/problems/house-robber/
'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        results = [0] * len(nums)
        results[0] = nums[0]
        results[1] = max(nums[0], nums[1])
        for index in range(2, len(nums)):
            results[index] = max(nums[index] + results[index-2], results[index-1])
        return results[len(nums) - 1]