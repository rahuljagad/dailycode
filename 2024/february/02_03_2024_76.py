'''
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
'''
from typing import Counter
from typing import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        answer = float("inf"), None, None
        # counter for the destination character counts.
        t_dict = Counter(t)
        s_dict = defaultdict(int)
        required = len(t_dict)          # should we do "t_dict.keys()??", i don't think so. 
        formed = 0
        # iterate from start to end of the string.
        while right < len(s):
            character = s[right]
            s_dict[character] = s_dict.get(character, 0) + 1
            # if the character counts matched then lets increment the formed
            # to see if they match the required.
            if s_dict[character] == t_dict[character]:
                formed += 1 

            while left <= right and formed == required:
                inner_character = s[left]
                if right - left + 1 < answer[0]:
                    answer = (right - left + 1, left, right)

                s_dict[inner_character] -= 1
                if inner_character in t_dict and s_dict[inner_character] < t_dict[inner_character]:
                    formed -= 1
                left += 1
            
            right += 1
        return "" if answer[0] == float("inf") else s[answer[1] : answer[2] + 1]