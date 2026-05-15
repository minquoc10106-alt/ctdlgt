# Last updated: 5/15/2026, 11:27:43 AM
1class Solution(object):
2    def findMaxConsecutiveOnes(self, nums):
3        lon_nhat = hien_tai = 0
4        for n in nums:
5            if n == 1:
6                hien_tai += 1
7                if hien_tai > lon_nhat: lon_nhat = hien_tai
8            else:
9                hien_tai = 0
10        return lon_nhat