# Last updated: 5/15/2026, 11:08:25 AM
1class Solution(object):
2    def firstBadVersion(self, n):
3        trai = 1
4        phai = n
5        while trai < phai:
6            giua = trai + (phai - trai) // 2
7            if isBadVersion(giua):
8                phai = giua
9            else:
10                trai = giua + 1
11        return trai