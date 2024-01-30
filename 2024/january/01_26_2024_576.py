'''
576. Out of Boundary Paths
Solved using recursion.
'''


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        ROWS, COLS = m, n
        cache = {}

        def find_path_recursion(row: int, col: int, remaining_moves: int):
            if row < 0 or row == ROWS or col < 0 or col == COLS:
                return 1
            if remaining_moves == 0:
                return 0
            if (row, col, remaining_moves) in cache:
                return cache[(row, col, remaining_moves)]
            cache[(row, col, remaining_moves)] = (
                find_path_recursion(row + 1, col, remaining_moves - 1) + 
                find_path_recursion(row - 1, col, remaining_moves - 1) +
                find_path_recursion(row, col + 1, remaining_moves - 1) +
                find_path_recursion(row, col - 1, remaining_moves - 1)) % MOD
            return cache[(row, col, remaining_moves)]
        
        return find_path_recursion(startRow, startColumn, maxMove)