'''
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        climb_stairs = [0] * (n + 1)
        climb_stairs[1], climb_stairs[2] = 1, 2
        for index in range(3, n + 1):
            climb_stairs[index] = climb_stairs[index-1] + climb_stairs[index-2]
        return climb_stairs[n]