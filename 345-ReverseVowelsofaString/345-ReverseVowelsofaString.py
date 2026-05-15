# Last updated: 5/15/2026, 11:10:53 AM
1class Solution(object):
2    def reverseVowels(self, s):
3        chars = list(s)
4        vowels = set("aeiouAEIOU") 
5        left, right = 0, len(chars) - 1
6        while left < right:
7            while left < right and chars[left] not in vowels:
8                left += 1
9            while left < right and chars[right] not in vowels:
10                right -= 1
11            chars[left], chars[right] = chars[right], chars[left]
12            left += 1
13            right -= 1
14            
15        return "".join(chars)