# Last updated: 5/15/2026, 9:58:51 AM
1class Solution(object):
2    def searchInsert(self, mang, tieu_chau):
3        trai = 0
4        phai = len(mang) - 1
5        while trai <= phai:
6            giua = (trai + phai) // 2          
7            if mang[giua] == tieu_chau:
8                return giua
9            elif mang[giua] < tieu_chau:
10                trai = giua + 1
11            else:
12                phai = giua - 1           
13        return trai