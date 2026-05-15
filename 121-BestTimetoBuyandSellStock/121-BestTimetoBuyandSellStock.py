# Last updated: 5/15/2026, 10:27:28 AM
1class Solution(object):
2    def maxProfit(self, gia):
3        loi = 0
4        for i in range(1, len(gia)):
5            if gia[i] > gia[i-1]:
6                loi += gia[i] - gia[i-1]
7        return loi