# Last updated: 5/15/2026, 10:24:22 AM
1class Solution(object):
2    def hasPathSum(self, goc, tong_muc_tieu):
3        if not goc:
4            return False
5        tong_muc_tieu -= goc.val
6        if not goc.left and not goc.right:
7            return tong_muc_tieu == 0
8        return (self.hasPathSum(goc.left, tong_muc_tieu) or 
9                self.hasPathSum(goc.right, tong_muc_tieu))