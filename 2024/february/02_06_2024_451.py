'''
451. Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/
'''
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        s_dict = Counter(s)
        max_frequency = max(s_dict.values())
        buckets = [ [] for _ in range(max_frequency + 1)]
        for char, frequency in s_dict.items():
            buckets[frequency].append(char)
        results = []
        for frequency_bucket in range(max_frequency, 0, -1):
            for character in buckets[frequency_bucket]:
                results.append(character * frequency_bucket)
        return "".join(results)