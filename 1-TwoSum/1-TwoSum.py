# Last updated: 5/15/2026, 9:45:02 AM
1class Solution(object):
2    def twoSum(self, nums, target):
3        # Create a dictionary to store the value and its index
4
5        prevMap = {} 
6
7        for i, n in enumerate(nums):
8            diff = target - n
9
10            if diff in prevMap:
11                return [prevMap[diff], i]
12
13            prevMap[n] = i