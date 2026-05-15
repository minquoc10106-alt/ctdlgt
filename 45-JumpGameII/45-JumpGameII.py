# Last updated: 5/15/2026, 9:36:55 AM
1class Solution(object):
2    def jump(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        if len(nums) <= 1:
8            return 0   
9        jumps = 0
10        current_end = 0
11        farthest = 0
12        for i in range(len(nums) - 1):
13            farthest = max(farthest, i + nums[i])
14            if i == current_end:
15                jumps += 1
16                current_end = farthest
17                if current_end >= len(nums) - 1:
18                    break             
19        return jumps