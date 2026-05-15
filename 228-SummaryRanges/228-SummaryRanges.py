# Last updated: 5/15/2026, 11:06:01 AM
1class Solution(object):
2    def summaryRanges(self, nums):
3        res = []
4        i = 0
5        while i < len(nums):
6            start = nums[i]
7            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
8                i += 1
9            if start != nums[i]:
10                res.append(str(start) + "->" + str(nums[i]))
11            else:
12                res.append(str(start))
13            i += 1
14        return res