# Last updated: 5/15/2026, 11:24:30 AM
1class Solution(object):
2    def thirdMax(self, nums):
3        tap = sorted(set(nums), reverse=True)
4        return tap[2] if len(tap) >= 3 else tap[0]