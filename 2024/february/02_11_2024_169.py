'''
169. Majority Element
https://leetcode.com/problems/majority-element/
'''
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        max_count, result = 0, 0
        for num, count in nums_count.items():
            if count > max_count:
                max_count = count
                result = num
        return result