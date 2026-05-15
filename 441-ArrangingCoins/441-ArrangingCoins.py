# Last updated: 5/15/2026, 11:25:11 AM
1class Solution(object):
2    def arrangeCoins(self, n):
3        trai, phai = 0, n
4        while trai <= phai:
5            giua = (trai + phai) // 2
6            tong = giua * (giua + 1) // 2
7            if tong == n: return giua
8            if n < tong: phai = giua - 1
9            else: trai = giua + 1
10        return phai