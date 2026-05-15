# Last updated: 5/15/2026, 10:10:26 AM
1class Solution(object):
2    def deleteDuplicates(self, head):
3        hien_tai = head
4        while hien_tai and hien_tai.next:
5            if hien_tai.val == hien_tai.next.val:
6                # Bỏ qua nút kế tiếp nếu nó trùng giá trị
7                hien_tai.next = hien_tai.next.next
8            else:
9                # Di chuyển sang nút tiếp theo nếu không trùng
10                hien_tai = hien_tai.next         
11        return head