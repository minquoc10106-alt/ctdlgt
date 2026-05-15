# Last updated: 5/15/2026, 11:28:55 AM
1class Solution(object):
2    def findPoisonedDuration(self, timeSeries, duration):
3        if not timeSeries: return 0
4        tong = 0
5        for i in range(len(timeSeries) - 1):
6            tong += min(timeSeries[i+1] - timeSeries[i], duration)
7        return tong + duration