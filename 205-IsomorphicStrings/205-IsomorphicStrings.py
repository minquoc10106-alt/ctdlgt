# Last updated: 5/15/2026, 11:04:38 AM
1class Solution(object):
2    def isIsomorphic(self, s, t):
3        map_s_to_t = {}
4        map_t_to_s = {}        
5        for char_s, char_t in zip(s, t):
6            if char_s in map_s_to_t:
7                if map_s_to_t[char_s] != char_t:
8                    return False
9            else:
10                map_s_to_t[char_s] = char_t
11            if char_t in map_t_to_s:
12                if map_t_to_s[char_t] != char_s:
13                    return False
14            else:
15                map_t_to_s[char_t] = char_s
16        return True