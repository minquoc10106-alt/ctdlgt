# Last updated: 5/15/2026, 9:52:12 AM
1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution(object):
8    def mergeTwoLists(self, list1, list2):
9        dummy = ListNode(0)
10        current = dummy
11        while list1 and list2:
12            if list1.val <= list2.val:
13                current.next = list1
14                list1 = list1.next
15            else:
16                current.next = list2
17                list2 = list2.next
18            current = current.next
19        if list1:
20            current.next = list1
21        elif list2:
22            current.next = list2
23        return dummy.next