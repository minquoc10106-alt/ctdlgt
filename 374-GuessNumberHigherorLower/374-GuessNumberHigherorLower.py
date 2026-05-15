# Last updated: 5/15/2026, 11:12:18 AM
1class Solution(object):
2    def guessNumber(self, n):
3        low = 1
4        high = n
5        while low <= high:
6            mid = low + (high - low) // 2
7            res = guess(mid)         
8            if res == 0:
9                return mid
10            elif res == -1:
11                high = mid - 1
12            else:
13                low = mid + 1