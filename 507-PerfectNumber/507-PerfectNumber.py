# Last updated: 5/15/2026, 11:30:29 AM
1class Solution(object):
2    def checkPerfectNumber(self, num):
3        if num <= 1: return False
4        tong = 1
5        can = int(num**0.5)
6        for i in range(2, can + 1):
7            if num % i == 0:
8                tong += i + num // i
9        if can * can == num: tong -= can
10        return tong == num