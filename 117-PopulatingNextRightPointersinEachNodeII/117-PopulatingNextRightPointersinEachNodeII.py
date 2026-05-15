# Last updated: 5/15/2026, 10:25:21 AM
1class Solution(object):
2    def connect(self, goc):
3        nay = goc
4        while nay:
5            gia = Node(0)
6            tam = gia
7            while nay:
8                if nay.left:
9                    tam.next = nay.left
10                    tam = tam.next
11                if nay.right:
12                    tam.next = nay.right
13                    tam = tam.next
14                nay = nay.next
15            nay = gia.next
16        return goc
17        