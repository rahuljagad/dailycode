'''
1657. Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/description/
'''
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        word1_dict = Counter(word1)
        word2_dict = Counter(word2)
        return word1_dict.keys() == word2_dict.keys() and sorted(word1_dict.values()) == sorted(word2_dict.values())