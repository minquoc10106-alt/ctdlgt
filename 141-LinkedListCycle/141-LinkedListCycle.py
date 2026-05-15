# Last updated: 5/15/2026, 10:32:26 AM
1class Solution(object):
2    def preorderTraversal(self, goc):
3        if not goc:
4            return []
5        kq = []
6        ngan_xep = [goc]
7
8        while ngan_xep:
9            nut = ngan_xep.pop()
10            kq.append(nut.val)    
11            if nut.right:
12                ngan_xep.append(nut.right)
13            if nut.left:
14                ngan_xep.append(nut.left) 
15        return kq