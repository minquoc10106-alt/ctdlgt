# Last updated: 5/15/2026, 10:30:05 AM
1class Solution(object):
2    def singleNumber(self, nums):
3        ket_qua = 0
4        for so in nums:
5            ket_qua ^= so
6        return ket_qua