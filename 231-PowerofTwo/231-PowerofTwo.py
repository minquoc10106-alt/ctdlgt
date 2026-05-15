# Last updated: 5/15/2026, 11:06:18 AM
1class Solution(object):
2    def isPowerOfTwo(self, n):
3        return n > 0 and (n & (n - 1)) == 0