# Last updated: 5/15/2026, 11:05:52 AM
1class Solution(object):
2    def invertTree(self, root):
3        if not root:
4            return None
5        root.left, root.right = root.right, root.left
6        self.invertTree(root.left)
7        self.invertTree(root.right) 
8        return root