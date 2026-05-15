# Last updated: 5/15/2026, 10:34:32 AM
1class Solution(object):
2    def postorderTraversal(self, root):
3        """
4        :type root: TreeNode
5        :rtype: List[int]
6        """
7        res = []
8        def dfs(node):
9            if not node:
10                return
11            dfs(node.left) 
12            dfs(node.right) 
13            res.append(node.val)
14            
15        dfs(root)
16        return res