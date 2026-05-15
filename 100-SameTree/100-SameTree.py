# Last updated: 5/15/2026, 10:11:41 AM
1class Solution(object):
2    def isSameTree(self, p, q):
3        if not p and not q:
4            return True
5        if not p or not q or p.val != q.val:
6            return False
7        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)