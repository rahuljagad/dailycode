'''
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_table = [ [ 0 for _ in range(len(text2) + 1) ] 
                    for _ in range(len(text1) + 1) ]

        for row in range(1, len(text1) + 1):
            for column in range(1, len(text2) + 1):
                if text1[row - 1] == text2[column - 1]:
                    dp_table[row][column] = 1 + dp_table[row - 1][column - 1]
                else: 
                    dp_table[row][column] = max(dp_table[row - 1][column],
                                                dp_table[row][column - 1])
        return dp_table[len(text1)][len(text2)]