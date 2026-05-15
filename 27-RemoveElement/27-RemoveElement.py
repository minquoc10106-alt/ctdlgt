# Last updated: 5/15/2026, 9:57:12 AM
1class Solution(object):
2    def removeElement(self, nums, val):
3        k = 0
4        for i in range(len(nums)):
5            if nums[i] != val:
6                nums[k] = nums[i]
7                k += 1
8        return k