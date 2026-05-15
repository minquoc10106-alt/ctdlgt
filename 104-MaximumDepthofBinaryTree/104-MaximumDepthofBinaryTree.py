# Last updated: 5/15/2026, 10:12:13 AM
1class Solution(object):
2    def maxDepth(self, goc):
3        if not goc:
4            return 0
5        trai = self.maxDepth(goc.left)
6        phai = self.maxDepth(goc.right)
7        return max(trai, phai) + 1