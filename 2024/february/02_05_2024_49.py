'''
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
'''
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = defaultdict(list)
        for word in strs:
            sorted_words["".join(sorted(word))].append(word)
        return [words for words in sorted_words.values()]