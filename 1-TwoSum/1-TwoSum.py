# Last updated: 5/15/2026, 9:44:25 AM
1class Solution(object):
2    def intToRoman(self, num):
3        bang_tra_cuu = [
4            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
5            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
6            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
7            (1 , "I")
8        ]
9        ket_qua = ""
10        for gia_tri, ky_hieu in bang_tra_cuu:
11            while num >= gia_tri:
12                ket_qua += ky_hieu
13                num -= gia_tri
14                
15        return ket_qua