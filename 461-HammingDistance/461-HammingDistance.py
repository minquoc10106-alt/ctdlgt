# Last updated: 5/15/2026, 11:26:39 AM
1class Solution(object):
2    def hammingDistance(self, x, y):
3        khac = x ^ y
4        return bin(khac).count('1')