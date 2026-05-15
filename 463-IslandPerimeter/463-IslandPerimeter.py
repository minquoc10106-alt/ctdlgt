# Last updated: 5/15/2026, 11:26:54 AM
1class Solution(object):
2    def islandPerimeter(self, grid):
3        hang, cot = len(grid), len(grid[0])
4        chu_vi = 0
5        for r in range(hang):
6            for c in range(cot):
7                if grid[r][c] == 1:
8                    chu_vi += 4
9                    if r > 0 and grid[r-1][c] == 1:
10                        chu_vi -= 2
11                    if c > 0 and grid[r][c-1] == 1:
12                        chu_vi -= 2
13        return chu_vi