# Last updated: 5/15/2026, 11:23:16 AM
1class Solution(object):
2    def sumOfLeftLeaves(self, goc):
3        if not goc: return 0
4        tong = 0
5        if goc.left and not goc.left.left and not goc.left.right:
6            tong += goc.left.val
7        return tong + self.sumOfLeftLeaves(goc.left) + self.sumOfLeftLeaves(goc.right)