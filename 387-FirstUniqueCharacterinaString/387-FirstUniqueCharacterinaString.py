# Last updated: 5/15/2026, 11:22:19 AM
1class Solution(object):
2    def firstUniqChar(self, s):
3        dem = {}
4        for chu in s:
5            dem[chu] = dem.get(chu, 0) + 1
6        for i, chu in enumerate(s):
7            if dem[chu] == 1:
8                return i
9        return -1