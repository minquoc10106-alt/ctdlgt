# Last updated: 5/15/2026, 11:26:23 AM
1class Solution(object):
2    def repeatedSubstringPattern(self, s):
3        chuoi_doi = (s + s)[1:-1]
4        return s in chuoi_doi