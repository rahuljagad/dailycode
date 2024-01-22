'''
645. Set Mismatch
https://leetcode.com/problems/set-mismatch/
'''
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        results = [0] * 2
        if len(nums) == 2:
            if nums[0] == 1 and nums[1] == 1:
                results[0], results[1] = 1, 2
            if nums[0] == 2 and nums[1] == 2:
                results[0], results[1] = 2, 1
        else:
            results[1] = 1 if nums[0] != 1 else 0
            index = 1
            prev_num = nums[0]
            while index < len(nums):
                if nums[index] - prev_num == 0:
                    results[0] = nums[index]
                if nums[index] - prev_num == 2:
                    results[1] = nums[index] - 1
                prev_num = nums[index]
                index += 1
            if results[1] == 0:
                results[1] = prev_num + 1
        return results