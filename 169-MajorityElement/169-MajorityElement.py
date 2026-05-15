# Last updated: 5/15/2026, 10:36:25 AM
1class Solution(object):
2    def majorityElement(self, nums):
3        ung_vien = None
4        phieu = 0
5        for so in nums:
6            if phieu == 0:
7                ung_vien = so
8            if so == ung_vien:
9                phieu += 1
10            else:
11                phieu -= 1
12        return ung_vien