# Last updated: 5/15/2026, 11:06:47 AM
1class Solution(object):
2    def isPalindrome(self, head):
3        slow = fast = head
4        while fast and fast.next:
5            slow = slow.next
6            fast = fast.next.next
7        prev = None
8        while slow:
9            nxt = slow.next
10            slow.next = prev
11            prev = slow
12            slow = nxt
13        left, right = head, prev
14        while right: # Chỉ cần kiểm tra đến hết nửa sau
15            if left.val != right.val:
16                return False
17            left = left.next
18            right = right.next
19            
20        return True