# Last updated: 5/15/2026, 11:03:56 AM
1class Solution(object):
2    def isHappy(self, n):
3        seen = set()
4        while n != 1:
5            n = sum(int(digit) ** 2 for digit in str(n))
6            if n in seen:
7                return False
8            seen.add(n)
9        return True