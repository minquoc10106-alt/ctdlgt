# Last updated: 5/15/2026, 11:27:03 AM
1class Solution(object):
2    def findComplement(self, num):
3        mat_na = (1 << num.bit_length()) - 1
4        return num ^ mat_na