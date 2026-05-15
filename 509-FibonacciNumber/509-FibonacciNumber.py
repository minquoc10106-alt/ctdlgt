# Last updated: 5/15/2026, 11:30:55 AM
1class Solution(object):
2    def fib(self, n):
3        if n <= 1: return n
4        a, b = 0, 1
5        for _ in range(2, n + 1):
6            a, b = b, a + b
7        return b