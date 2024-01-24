'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
'''

class Solution:
    def fib(self, n: int) -> int:
        sequence = [0,1]
        if n <= 1:
            return n
        for i in range(2, n+1):
            sequence.append(sequence[i-1] + sequence[i-2])
        return sequence[-1]