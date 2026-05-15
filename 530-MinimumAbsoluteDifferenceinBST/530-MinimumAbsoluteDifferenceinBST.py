# Last updated: 5/15/2026, 11:31:34 AM
1class Solution(object):
2    def getMinimumDifference(self, root):
3        self.min_cly = float('inf')
4        self.truoc = -float('inf')
5        def duyet(nut):
6            if not nut: return
7            duyet(nut.left)
8            self.min_cly = min(self.min_cly, nut.val - self.truoc)
9            self.truoc = nut.val
10            duyet(nut.right)     
11        duyet(root)
12        return self.min_cly