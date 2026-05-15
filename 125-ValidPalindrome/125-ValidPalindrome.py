# Last updated: 5/15/2026, 10:29:49 AM
1class Solution(object):
2    def isPalindrome(self, s):
3        trai = 0
4        phai = len(s) - 1
5        while trai < phai:
6            while trai < phai and not s[trai].isalnum():
7                trai += 1
8            while trai < phai and not s[phai].isalnum():
9                phai -= 1
10            if s[trai].lower() != s[phai].lower():
11                return False
12            trai += 1
13            phai -= 1         
14        return True