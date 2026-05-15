# Last updated: 5/15/2026, 9:49:57 AM
1class Solution(object):
2    def longestCommonPrefix(self, danh_sach_chuoi):
3        """
4        :type danh_sach_chuoi: List[str]
5        :rtype: str
6        """
7        if not danh_sach_chuoi:
8            return ""
9        tien_to = danh_sach_chuoi[0]
10        for i in range(1, len(danh_sach_chuoi)):
11            chuoi_hien_tai = danh_sach_chuoi[i]
12            while not chuoi_hien_tai.startswith(tien_to):
13                tien_to = tien_to[:-1]
14                if not tien_to:
15                    return ""       
16        return tien_to