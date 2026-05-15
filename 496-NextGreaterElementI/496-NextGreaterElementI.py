# Last updated: 5/15/2026, 11:29:05 AM
1class Solution(object):
2    def nextGreaterElement(self, nums1, nums2):
3        dic = {}
4        ngan_xep = []
5        for so in nums2:
6            while ngan_xep and ngan_xep[-1] < so:
7                dic[ngan_xep.pop()] = so
8            ngan_xep.append(so)
9        return [dic.get(so, -1) for so in nums1]