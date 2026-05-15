# Last updated: 5/15/2026, 11:08:36 AM
1class Solution(object):
2    def moveZeroes(self, nums):
3        vt_khac_0 = 0
4        for i in range(len(nums)):
5            if nums[i] != 0:
6                nums[vt_khac_0], nums[i] = nums[i], nums[vt_khac_0]
7                vt_khac_0 += 1