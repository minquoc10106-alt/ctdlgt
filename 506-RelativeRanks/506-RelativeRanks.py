# Last updated: 5/15/2026, 11:30:06 AM
1class Solution(object):
2    def findRelativeRanks(self, diem):
3        sap_xep = sorted(diem, reverse=True)
4        hang = {}
5        for i, d in enumerate(sap_xep):
6            if i == 0: hang[d] = "Gold Medal"
7            elif i == 1: hang[d] = "Silver Medal"
8            elif i == 2: hang[d] = "Bronze Medal"
9            else: hang[d] = str(i + 1)
10        
11        return [hang[d] for d in diem]