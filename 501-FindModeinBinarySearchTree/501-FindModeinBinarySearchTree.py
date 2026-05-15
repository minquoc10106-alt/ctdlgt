# Last updated: 5/15/2026, 11:29:35 AM
1class Solution(object):
2    def findMode(self, goc):
3        dem = {}
4        def duyet(nut):
5            if not nut: return
6            dem[nut.val] = dem.get(nut.val, 0) + 1
7            duyet(nut.left)
8            duyet(nut.right)
9        
10        duyet(goc)
11        lon_nhat = max(dem.values())
12        return [so for so, sl in dem.items() if sl == lon_nhat]