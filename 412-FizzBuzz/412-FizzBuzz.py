# Last updated: 5/15/2026, 11:24:08 AM
1class Solution(object):
2    def fizzBuzz(self, n):
3        kq = []
4        for i in range(1, n + 1):
5            if i % 3 == 0 and i % 5 == 0:
6                kq.append("FizzBuzz")
7            elif i % 3 == 0:
8                kq.append("Fizz")
9            elif i % 5 == 0:
10                kq.append("Buzz")
11            else:
12                kq.append(str(i))
13        return kq