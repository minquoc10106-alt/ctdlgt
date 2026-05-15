# Last updated: 5/15/2026, 9:58:29 AM
1class Solution(object):
2    def strStr(self, nguon, mau):
3        n = len(nguon)
4        m = len(mau)
5        for i in range(n - m + 1):
6            if nguon[i : i + m] == mau:
7                return i 
8        return -1