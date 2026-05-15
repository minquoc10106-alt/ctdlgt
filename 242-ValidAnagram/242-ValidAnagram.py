# Last updated: 5/15/2026, 11:07:04 AM
1class Solution(object):
2    def isAnagram(self, s, t):
3        if len(s) != len(t):
4            return False
5        dem = {}
6        for ky_tu in s:
7            dem[ky_tu] = dem.get(ky_tu, 0) + 1
8        for ky_tu in t:
9            if ky_tu not in dem or dem[ky_tu] == 0:
10                return False
11            dem[ky_tu] -= 1
12        return True