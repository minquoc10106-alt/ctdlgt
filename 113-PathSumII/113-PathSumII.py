# Last updated: 5/15/2026, 10:24:38 AM
1class Solution(object):
2    def pathSum(self, goc, tong):
3        kq = []
4        def duyet(n, con, t):
5            if not n: return
6            con.append(n.val)
7            if not n.left and not n.right and sum(con) == t:
8                kq.append(list(con))
9            duyet(n.left, con, t)
10            duyet(n.right, con, t)
11            con.pop()
12        duyet(goc, [], tong)
13        return kq