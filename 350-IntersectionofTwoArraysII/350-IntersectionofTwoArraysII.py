# Last updated: 5/15/2026, 11:11:31 AM
1class Solution(object):
2    def intersect(self, nums1, nums2):
3        nums1.sort() # Bỏ qua nếu mảng đã sắp xếp sẵn
4        nums2.sort()       
5        i = j = 0
6        res = []  
7        while i < len(nums1) and j < len(nums2):
8            if nums1[i] < nums2[j]:
9                i += 1
10            elif nums1[i] > nums2[j]:
11                j += 1
12            else:
13                res.append(nums1[i])
14                i += 1
15                j += 1
16        return res