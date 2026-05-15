# Last updated: 5/15/2026, 10:27:03 AM
1class Solution(object):
2    def minimumTotal(self, tam_giac):
3        for hinh in range(len(tam_giac) - 2, -1, -1):
4            for cot in range(len(tam_giac[hinh])):
5                tam_giac[hinh][cot] += min(tam_giac[hinh+1][cot], tam_giac[hinh+1][cot+1])
6        return tam_giac[0][0]