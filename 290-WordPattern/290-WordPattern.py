# Last updated: 5/15/2026, 11:08:55 AM
1class Solution(object):
2    def wordPattern(self, pattern, s):
3        words = s.split()
4        # Nếu số lượng ký tự trong pattern khác số lượng từ trong s
5        if len(pattern) != len(words):
6            return False
7        # Kiểm tra tính đồng nhất bằng cách so sánh vị trí xuất hiện đầu tiên
8        # pattern = "abba", s = "dog cat cat dog"
9        # map(pattern.find, pattern) -> [0, 1, 1, 0]
10        # map(words.index, words)     -> [0, 1, 1, 0]
11        return list(map(pattern.find, pattern)) == list(map(words.index, words))