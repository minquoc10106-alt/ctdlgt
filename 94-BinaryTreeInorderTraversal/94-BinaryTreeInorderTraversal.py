# Last updated: 5/15/2026, 10:11:28 AM
1class Solution(object):
2    def inorderTraversal(self, goc):
3        kq = []
4        ngan_xep = []
5        hien_tai = goc
6        while hien_tai or ngan_xep:
7            while hien_tai:
8                ngan_xep.append(hien_tai)
9                hien_tai = hien_tai.left
10            hien_tai = ngan_xep.pop()
11            kq.append(hien_tai.val)
12            hien_tai = hien_tai.right
13        return kq