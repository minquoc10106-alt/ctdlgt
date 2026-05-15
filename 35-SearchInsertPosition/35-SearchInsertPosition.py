# Last updated: 5/15/2026, 9:59:28 AM
1class Solution(object):
2    def isValidSudoku(self, bang):
3        hang = [set() for _ in range(9)]
4        cot = [set() for _ in range(9)]
5        o_vuong = [set() for _ in range(9)]
6        for r in range(9):
7            for c in range(9):
8                so = bang[r][c] 
9                if so == ".":
10                    continue
11                vi_tri_o = (r // 3) * 3 + (c // 3)
12                if (so in hang[r] or 
13                    so in cot[c] or 
14                    so in o_vuong[vi_tri_o]):
15                    return False
16                hang[r].add(so)
17                cot[c].add(so)
18                o_vuong[vi_tri_o].add(so)
19                
20        return True