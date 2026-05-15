# Last updated: 5/15/2026, 11:25:55 AM
1class Solution(object):
2    def findDisappearedNumbers(self, nums):
3        for n in nums:
4            vi_tri = abs(n) - 1
5            if nums[vi_tri] > 0:
6                nums[vi_tri] *= -1
7        
8        kq = []
9        for i in range(len(nums)):
10            if nums[i] > 0:
11                kq.append(i + 1)
12        return kq