# Last updated: 5/15/2026, 11:31:03 AM
1class Solution(object):
2    def detectCapitalUse(self, word):
3        return word.isupper() or word.islower() or word.istitle()