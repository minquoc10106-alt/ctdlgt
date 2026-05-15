# Last updated: 5/15/2026, 11:07:17 AM
1class Solution(object):
2    def binaryTreePaths(self, root):
3        kq = []
4        def duyet(nut, duong_di):
5            if nut:
6                duong_di += str(nut.val)
7                if not nut.left and not nut.right:
8                    kq.append(duong_di)
9                else:
10                    duong_di += "->"
11                    duyet(nut.left, duong_di)
12                    duyet(nut.right, duong_di)
13        duyet(root, "")
14        return kq