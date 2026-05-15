# Last updated: 5/15/2026, 11:23:23 AM
1class Solution(object):
2    def toHex(self, num):
3        if num == 0: return "0"
4        bang = "0123456789abcdef"
5        kq = ""
6        num &= 0xFFFFFFFF
7        while num > 0:
8            kq = bang[num % 16] + kq
9            num //= 16
10        return kq