# Last updated: 5/15/2026, 11:28:30 AM
1class Solution(object):
2    def constructRectangle(self, area):
3        rong = int(area**0.5)
4        while area % rong != 0:
5            rong -= 1
6        return [area // rong, rong]