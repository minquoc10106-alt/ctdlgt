# Last updated: 5/15/2026, 11:12:08 AM
1class Solution(object):
2    def isPerfectSquare(self, num):
3        if num < 2:
4            return True
5        left, right = 2, num // 2
6        while left <= right:
7            mid = left + (right - left) // 2
8            guess = mid * mid
9            if guess == num:
10                return True
11            if guess > num:
12                right = mid - 1
13            else:
14                left = mid + 1  
15        return False