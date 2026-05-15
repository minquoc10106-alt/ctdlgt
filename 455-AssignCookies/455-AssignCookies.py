# Last updated: 5/15/2026, 11:26:03 AM
1class Solution(object):
2    def findContentChildren(self, g, s):
3        g.sort()
4        s.sort()
5        tre, banh = 0, 0
6        while tre < len(g) and banh < len(s):
7            if s[banh] >= g[tre]:
8                tre += 1
9            banh += 1
10        return tre