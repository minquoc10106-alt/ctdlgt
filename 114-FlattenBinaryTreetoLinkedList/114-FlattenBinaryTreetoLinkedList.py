# Last updated: 5/15/2026, 10:24:46 AM
1class Solution(object):
2    def flatten(self, goc):
3        nay = goc
4        while nay:
5            if nay.left:
6                trai = nay.left
7                while trai.right: trai = trai.right
8                trai.right = nay.right
9                nay.right = nay.left
10                nay.left = None
11            nay = nay.right