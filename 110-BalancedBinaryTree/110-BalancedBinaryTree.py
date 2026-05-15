# Last updated: 5/15/2026, 10:12:49 AM
1class Solution(object):
2    def isBalanced(self, goc):
3        return self.kiem_tra_chieu_cao(goc) != -1
4    def kiem_tra_chieu_cao(self, nut):
5        if not nut:
6            return 0
7        trai = self.kiem_tra_chieu_cao(nut.left)
8        if trai == -1: return -1 
9        phai = self.kiem_tra_chieu_cao(nut.right)
10        if phai == -1: return -1
11        if abs(trai - phai) > 1:
12            return -1
13        return max(trai, phai) + 1