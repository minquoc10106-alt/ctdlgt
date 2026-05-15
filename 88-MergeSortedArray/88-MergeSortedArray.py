# Last updated: 5/15/2026, 10:11:06 AM
1class Solution(object):
2    def merge(self, mang1, m, mang2, n):
3        i = m - 1      
4        j = n - 1     
5        k = m + n - 1  
6        while j >= 0:
7            if i >= 0 and mang1[i] > mang2[j]:
8                mang1[k] = mang1[i]
9                i -= 1
10            else:
11                mang1[k] = mang2[j]
12                j -= 1
13            k -= 1