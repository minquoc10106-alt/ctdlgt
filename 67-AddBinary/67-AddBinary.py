# Last updated: 5/15/2026, 10:09:52 AM
1class Solution(object):
2    def addBinary(self, a, b):
3        kq = []
4        nho = 0
5        i = len(a) - 1
6        j = len(b) - 1
7        while i >= 0 or j >= 0 or nho:
8            tong = nho
9            if i >= 0:
10                tong += int(a[i])
11                i -= 1
12            if j >= 0:
13                tong += int(b[j])
14                j -= 1
15            kq.append(str(tong % 2))
16            nho = tong // 2 
17        return "".join(reversed(kq))