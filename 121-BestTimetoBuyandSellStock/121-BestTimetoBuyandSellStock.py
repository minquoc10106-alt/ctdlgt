# Last updated: 5/15/2026, 10:27:18 AM
1class Solution(object):
2    def maxProfit(self, gia_ca):
3        loi_nhuan_max = 0
4        gia_thap_nhat = float('inf')       
5        for gia in gia_ca:
6            if gia < gia_thap_nhat:
7                gia_thap_nhat = gia
8            loi_nhuan_hien_tai = gia - gia_thap_nhat
9            if loi_nhuan_hien_tai > loi_nhuan_max:
10                loi_nhuan_max = loi_nhuan_hien_tai               
11        return loi_nhuan_max