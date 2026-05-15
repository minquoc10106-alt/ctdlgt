# Last updated: 5/15/2026, 10:12:37 AM
1class Solution(object):
2    def sortedArrayToBST(self, mang):
3        if not mang:
4            return None
5        giua = len(mang) // 2       
6        goc = TreeNode(mang[giua])
7        goc.left = self.sortedArrayToBST(mang[:giua])
8        goc.right = self.sortedArrayToBST(mang[giua + 1:])
9        return goc