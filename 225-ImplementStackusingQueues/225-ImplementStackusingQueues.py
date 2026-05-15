# Last updated: 5/15/2026, 11:05:33 AM
1from collections import deque
2
3class MyStack(object):
4    def __init__(self):
5        self.queue = deque()
6    def push(self, x):
7        self.queue.append(x)
8        for _ in range(len(self.queue) - 1):
9            self.queue.append(self.queue.popleft())
10    def pop(self):
11        return self.queue.popleft()
12    def top(self):
13        return self.queue[0]
14    def empty(self):
15        return not self.queue