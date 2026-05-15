# Last updated: 5/15/2026, 11:04:06 AM
1class Solution(object):
2    def removeElements(self, head, val):
3        dummy = ListNode(0)
4        dummy.next = head
5        current = dummy     
6        while current.next:
7            if current.next.val == val:
8                current.next = current.next.next
9            else:
10                current = current.next
11        return dummy.next
12        