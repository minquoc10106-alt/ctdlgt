# Last updated: 5/15/2026, 11:08:13 AM
1class Solution(object):
2    def missingNumber(self, nums):
3        n = len(nums)
4        tong_ly_thuyet = n * (n + 1) // 2
5        tong_thuc_te = sum(nums)
6        return tong_ly_thuyet - tong_thuc_te