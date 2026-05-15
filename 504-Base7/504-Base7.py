# Last updated: 5/15/2026, 11:29:56 AM
1class Solution(object):
2    def convertToBase7(self, num):
3        if num == 0: return "0"
4        so = abs(num)
5        kq = ""
6        while so:
7            kq = str(so % 7) + kq
8            so //= 7
9        return ("-" if num < 0 else "") + kq