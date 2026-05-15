# Last updated: 5/15/2026, 10:09:41 AM
1class Solution(object):
2    def mySqrt(self, x):
3        if x < 2:
4            return x 
5        trai = 2
6        phai = x // 2   
7        while trai <= phai:
8            giua = (trai + phai) // 2
9            binh_phuong = giua * giua         
10            if binh_phuong == x:
11                return giua
12            elif binh_phuong < x:
13                trai = giua + 1
14            else:
15                phai = giua - 1      
16        return phai