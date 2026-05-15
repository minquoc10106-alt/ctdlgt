# Last updated: 5/15/2026, 10:25:13 AM
1class Solution(object):
2    def connect(self, goc):
3        hang = goc
4        while hang and hang.left:
5            nay = hang
6            while nay:
7                nay.left.next = nay.right
8                if nay.next:
9                    nay.right.next = nay.next.left
10                nay = nay.next
11            hang = hang.left
12        return goc