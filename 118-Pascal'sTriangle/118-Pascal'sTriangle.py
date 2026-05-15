# Last updated: 5/15/2026, 10:26:33 AM
1class Solution(object):
2    def generate(self, n):
3        tg = []      
4        for i in range(n):
5            hang = [1] * (i + 1)
6            for j in range(1, i):
7                hang[j] = tg[i-1][j-1] + tg[i-1][j] 
8            tg.append(hang)
9        return tg