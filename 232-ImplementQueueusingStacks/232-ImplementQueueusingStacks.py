# Last updated: 5/15/2026, 11:06:35 AM
1class MyQueue(object):
2    def __init__(self):
3        self.stack_in = []
4        self.stack_out = []
5
6    def push(self, x):
7        self.stack_in.append(x)
8
9    def pop(self):
10        self.move_if_needed()
11        return self.stack_out.pop()
12
13    def peek(self):
14        self.move_if_needed()
15        return self.stack_out[-1]
16
17    def empty(self):
18        return not self.stack_in and not self.stack_out
19
20    def move_if_needed(self):
21        if not self.stack_out:
22            while self.stack_in:
23                self.stack_out.append(self.stack_in.pop())