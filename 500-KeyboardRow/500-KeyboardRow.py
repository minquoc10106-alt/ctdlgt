# Last updated: 5/15/2026, 11:29:26 AM
1class Solution(object):
2    def findWords(self, words):
3        hang1 = set("qwertyuiop")
4        hang2 = set("asdfghjkl")
5        hang3 = set("zxcvbnm")
6        kq = []
7        for chu in words:
8            tap_chu = set(chu.lower())
9            if tap_chu <= hang1 or tap_chu <= hang2 or tap_chu <= hang3:
10                kq.append(chu)
11        return kq