# Last updated: 5/15/2026, 11:09:40 AM
1import math
2
3class Solution(object):
4    def isPowerOfThree(self, n):
5        if n <= 0:
6            return False
7        # Tính log cơ số 3 của n
8        res = math.log10(n) / math.log10(3)
9        return res % 1 == 0