# Last updated: 5/15/2026, 11:31:47 AM
1class Solution(object):
2    def reverseStr(self, s, k):
3        mang = list(s)
4        for i in range(0, len(mang), 2 * k):
5            mang[i:i+k] = reversed(mang[i:i+k])
6        return "".join(mang)