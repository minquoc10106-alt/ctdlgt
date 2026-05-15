# Last updated: 5/15/2026, 10:12:04 AM
1class Solution(object):
2    def isSymmetric(self, goc):
3        if not goc:
4            return True
5        return self.kiem_tra(goc.left, goc.right)
6    def kiem_tra(self, trai, phai):
7        if not trai and not phai:
8            return True
9        if not trai or not phai or trai.val != phai.val:
10            return False
11        return (self.kiem_tra(trai.left, phai.right) and 
12                self.kiem_tra(trai.right, phai.left))