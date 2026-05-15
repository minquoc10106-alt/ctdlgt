# Last updated: 5/15/2026, 9:49:22 AM
1class Solution(object):
2    def romanToInt(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        roman_map = {
8            'I': 1,
9            'V': 5,
10            'X': 10,
11            'L': 50,
12            'C': 100,
13            'D': 500,
14            'M': 1000
15        }
16        total = 0
17        n = len(s)
18        for i in range(n):
19            if i < n - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
20                total -= roman_map[s[i]]
21            else:
22                total += roman_map[s[i]]              
23        return total