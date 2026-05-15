# Last updated: 5/15/2026, 11:22:42 AM
1class Solution(object):
2    def isSubsequence(self, s, t):
3        i = j = 0
4        while i < len(s) and j < len(t):
5            if s[i] == t[j]:
6                i += 1
7            j += 1
8        return i == len(s)