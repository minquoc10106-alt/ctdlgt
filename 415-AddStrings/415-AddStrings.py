# Last updated: 5/15/2026, 11:25:29 AM
1class Solution(object):
2    def addStrings(self, num1, num2):
3        kq = []
4        nho = 0
5        i, j = len(num1) - 1, len(num2) - 1
6        while i >= 0 or j >= 0 or nho:
7            v1 = ord(num1[i]) - ord('0') if i >= 0 else 0
8            v2 = ord(num2[j]) - ord('0') if j >= 0 else 0
9            tong = v1 + v2 + nho
10            kq.append(str(tong % 10))
11            nho = tong // 10
12            i -= 1
13            j -= 1
14        return "".join(kq[::-1])