# Last updated: 5/15/2026, 11:10:41 AM
1class Solution(object):
2    def reverseString(self, s):
3        """
4        :type s: List[str]
5        :rtype: None Do not return anything, modify s in-place instead.
6        """
7        left = 0
8        right = len(s) - 1
9        
10        while left < right:
11            s[left], s[right] = s[right], s[left]
12            left += 1
13            right -= 1