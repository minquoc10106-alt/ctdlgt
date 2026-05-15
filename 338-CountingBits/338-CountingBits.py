# Last updated: 5/15/2026, 11:10:01 AM
1class Solution(object):
2    def countBits(self, n):
3        ans = [0] * (n + 1)
4        for i in range(1, n + 1):
5            ans[i] = ans[i & (i - 1)] + 1
6        return ans