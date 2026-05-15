# Last updated: 5/15/2026, 11:11:10 AM
1class Solution(object):
2    def intersection(self, nums1, nums2):
3        nums1.sort()
4        nums2.sort()
5        res = set()
6        i = j = 0
7        
8        while i < len(nums1) and j < len(nums2):
9            if nums1[i] == nums2[j]:
10                res.add(nums1[i])
11                i += 1
12                j += 1
13            elif nums1[i] < nums2[j]:
14                i += 1
15            else:
16                j += 1
17        return list(res)