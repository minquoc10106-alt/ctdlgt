# Last updated: 5/15/2026, 11:32:00 AM
1class Solution(object):
2    def diameterOfBinaryTree(self, root):
3        self.duong_kinh = 0
4        def cao(nut):
5            if not nut: return 0
6            trai = cao(nut.left)
7            phai = cao(nut.right)
8            self.duong_kinh = max(self.duong_kinh, trai + phai)
9            return 1 + max(trai, phai)
10        cao(root)
11        return self.duong_kinh