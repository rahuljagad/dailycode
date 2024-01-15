'''
2225. Find Players With Zero or One Losses
https://leetcode.com/problems/find-players-with-zero-or-one-losses/
'''
from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_count = defaultdict(int)
        for match in matches:
            lost_count[match[0]] = lost_count.get(match[0], 0)
            lost_count[match[1]] = lost_count.get(match[1], 0) + 1
        results = [[] for _ in range(2)]
        for player, count in lost_count.items():
            if count == 0:
                results[0].append(player)
            if count == 1:
                results[1].append(player)
        results[0] = sorted(results[0])
        results[1] = sorted(results[1])
        return results