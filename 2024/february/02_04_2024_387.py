'''
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/
'''
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counters = Counter(s) 
        for index, character in enumerate(s):
            if counters[character] == 1:
                return index
        return -1