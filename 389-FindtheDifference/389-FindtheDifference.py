# Last updated: 5/15/2026, 11:22:29 AM
1class Solution(object):
2    def findTheDifference(self, s, t):
3        tong = 0
4        for chu in t: tong += ord(chu)
5        for chu in s: tong -= ord(chu)
6        return chr(tong)