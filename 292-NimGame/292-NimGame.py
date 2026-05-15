# Last updated: 5/15/2026, 11:09:08 AM
1class Solution(object):
2    def canWinNim(self, n):
3        """
4        :type n: int
5        :rtype: bool
6        """
7        # Bạn chỉ thua nếu n là bội số của 4
8        return n % 4 != 0