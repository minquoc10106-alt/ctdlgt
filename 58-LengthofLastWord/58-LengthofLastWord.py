# Last updated: 5/15/2026, 10:08:35 AM
1class Solution(object):
2    def lengthOfLastWord(self, s):
3        do_dai = 0
4        i = len(s) - 1
5        while i >= 0 and s[i] == ' ':
6            i -= 1
7        while i >= 0 and s[i] != ' ':
8            do_dai += 1
9            i -= 1
10        return do_dai