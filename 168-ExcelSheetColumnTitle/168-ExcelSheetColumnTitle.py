# Last updated: 5/15/2026, 10:36:02 AM
1class Solution(object):
2    def convertToTitle(self, n):
3        kq = []
4        while n > 0:
5            n -= 1
6            du = n % 26
7            kq.append(chr(du + ord('A')))
8            n //= 26
9        return "".join(reversed(kq))