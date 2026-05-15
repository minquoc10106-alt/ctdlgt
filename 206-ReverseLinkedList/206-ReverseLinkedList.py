# Last updated: 5/15/2026, 11:04:47 AM
1class Solution(object):
2    def reverseList(self, head):
3        prev = None
4        curr = head
5        while curr:
6            next_node = curr.next  # Lưu lại node tiếp theo
7            curr.next = prev       # Đảo chiều mũi tên
8            prev = curr            # Tiến prev lên vị trí hiện tại
9            curr = next_node       # Tiến curr lên vị trí tiếp theo
10        return prev