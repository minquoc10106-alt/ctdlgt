# Last updated: 5/15/2026, 10:10:18 AM
1class Solution(object):
2    def climbStairs(self, n):
3        if n <= 2:
4            return n    
5        truoc_2 = 1 # Bậc n-2
6        truoc_1 = 2 # Bậc n-1
7        for i in range(3, n + 1):
8            hien_tai = truoc_1 + truoc_2
9            truoc_2 = truoc_1
10            truoc_1 = hien_tai
11        return truoc_1