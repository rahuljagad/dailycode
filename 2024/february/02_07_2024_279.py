'''
279. Perfect Squares
https://leetcode.com/problems/perfect-squares/
'''


class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for index in range(1, n + 1):
            if index * index > n:
                break
            squares.append(index * index)
    
        results = [0] * (n + 1)
        results[1] = 1
        for value in range(2, n + 1):
            min_val = float("inf")
            for square in squares:
                if square > value:
                    break
                if value == square:
                    min_val = 1
                    break
                else:
                    min_val = min(min_val, results[value - square] + results[square])
            results[value] = min_val
        return results[n]