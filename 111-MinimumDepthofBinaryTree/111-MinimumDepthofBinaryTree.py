# Last updated: 5/15/2026, 10:24:12 AM
1class Solution(object):
2    def minDepth(self, goc):
3        if not goc:
4            return 0
5        if not goc.left and not goc.right:
6            return 1
7
8        if not goc.left:
9            return self.minDepth(goc.right) + 1
10        if not goc.right:
11            return self.minDepth(goc.left) + 1
12        return min(self.minDepth(goc.left), self.minDepth(goc.right)) + 1