# Last updated: 5/15/2026, 10:08:46 AM
1class Solution(object):
2    def plusOne(self, mang_so):
3        n = len(mang_so)      
4        for i in range(n - 1, -1, -1):
5            if mang_so[i] < 9:
6                mang_so[i] += 1
7                return mang_so
8            mang_so[i] = 0
9        return [1] + mang_so