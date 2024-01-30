'''
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = 0
                if token == '+':
                    result = operand1 + operand2 
                if token == '-':
                    result = operand1 - operand2 
                if token == '*':
                    result = operand1 * operand2
                if token == '/':
                    result = int(operand1 / operand2)
                stack.append(result)
            else:
                stack.append(int(token))
        
        final_result = stack.pop()
        return final_result