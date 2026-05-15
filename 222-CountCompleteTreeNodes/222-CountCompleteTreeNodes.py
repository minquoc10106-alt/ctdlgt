# Last updated: 5/15/2026, 11:05:24 AM
1class Solution(object):
2    def countNodes(self, root):
3        if not root:
4            return 0
5        def get_height_left(node):
6            h = 0
7            while node:
8                h += 1
9                node = node.left
10            return h
11        def get_height_right(node):
12            h = 0
13            while node:
14                h += 1
15                node = node.right
16            return h
17        left_h = get_height_left(root)
18        right_h = get_height_right(root)
19        if left_h == right_h:
20            return (2 ** left_h) - 1
21        return 1 + self.countNodes(root.left) + self.countNodes(root.right)