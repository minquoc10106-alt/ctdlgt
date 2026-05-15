# Last updated: 5/15/2026, 11:04:55 AM
1class Solution(object):
2    def containsDuplicate(self, nums):
3        return len(nums) != len(set(nums))