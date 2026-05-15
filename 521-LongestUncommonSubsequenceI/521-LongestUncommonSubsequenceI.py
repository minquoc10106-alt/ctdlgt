# Last updated: 5/15/2026, 11:31:23 AM
1class Solution(object):
2    def findLUSlength(self, a, b):
3        if a == b:
4            return -1
5        return max(len(a), len(b))