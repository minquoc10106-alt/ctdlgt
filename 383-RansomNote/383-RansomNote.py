# Last updated: 5/15/2026, 11:12:39 AM
1from collections import Counter
2
3class Solution(object):
4    def canConstruct(self, ransomNote, magazine):
5        """
6        :type ransomNote: str
7        :type magazine: str
8        :rtype: bool
9        """
10        # Đếm số lượng từng ký tự trong magazine
11        counts = Counter(magazine)
12        # Kiểm tra từng ký tự trong ransomNote
13        for char in ransomNote:
14            if counts[char] <= 0:
15                return False
16            counts[char] -= 1
17        return True