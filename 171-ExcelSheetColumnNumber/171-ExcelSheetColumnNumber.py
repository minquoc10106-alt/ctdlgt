# Last updated: 5/15/2026, 10:36:34 AM
1class Solution(object):
2    def titleToNumber(self, columnTitle):
3        kq = 0
4        for ky_tu in columnTitle:
5            so = ord(ky_tu) - ord('A') + 1
6            kq = kq * 26 + so
7        return kq