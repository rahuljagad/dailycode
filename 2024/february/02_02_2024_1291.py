'''
1291. Sequential Digits
https://leetcode.com/problems/sequential-digits/
'''
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        results = []
        low_length, high_length = len(str(low)), len(str(high))
        for digits in range(low_length, high_length + 1):
            for start in range(1, 10):
                if start + digits > 10:
                    break
                num = start
                prev = start
                for _ in range(1, digits):
                    num = num * 10
                    prev += 1
                    num += prev
                if low <= num <= high:
                    results.append(num)
        return results