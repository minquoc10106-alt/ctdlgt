# Last updated: 5/15/2026, 11:27:34 AM
1class Solution(object):
2    def licenseKeyFormatting(self, s, k):
3        chu = s.replace("-", "").upper()
4        n = len(chu)
5        dau = n % k
6        kq = []
7        if dau > 0:
8            kq.append(chu[:dau])
9        for i in range(dau, n, k):
10            kq.append(chu[i:i+k]) 
11        return "-".join(kq)