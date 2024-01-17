'''
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/
'''
from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = Counter(arr)
        occurence_set = set()
        for key, value in occurences.items():
            if value in occurence_set:
                return False
            occurence_set.add(value)
        return True