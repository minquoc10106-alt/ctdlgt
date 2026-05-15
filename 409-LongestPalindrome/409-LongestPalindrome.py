# Last updated: 5/15/2026, 11:23:44 AM
1class Solution(object):
2    def longestPalindrome(self, s):
3        dem = {}
4        for chu in s:
5            dem[chu] = dem.get(chu, 0) + 1
6        
7        do_dai = 0
8        le = False
9        for sl in dem.values():
10            if sl % 2 == 0:
11                do_dai += sl
12            else:
13                do_dai += sl - 1
14                le = True
15        
16        return do_dai + 1 if le else do_dai