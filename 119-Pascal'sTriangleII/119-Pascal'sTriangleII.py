# Last updated: 5/15/2026, 10:26:41 AM
1class Solution(object):
2    def getRow(self, chi_so_hang):
3        hang = [1] * (chi_so_hang + 1)     
4        for i in range(2, chi_so_hang + 1):
5            for j in range(i - 1, 0, -1):
6                hang[j] = hang[j] + hang[j-1]   
7        return hang