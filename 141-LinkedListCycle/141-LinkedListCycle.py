# Last updated: 5/15/2026, 10:32:16 AM
1class Solution(object):
2    def hasCycle(self, head):
3        rua = head
4        tho = head
5        
6        while tho and tho.next:
7            rua = rua.next         
8            tho = tho.next.next     
9            if rua == tho:
10                return True
11        return False