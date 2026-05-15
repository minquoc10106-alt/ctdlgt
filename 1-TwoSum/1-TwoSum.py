# Last updated: 5/15/2026, 9:42:18 AM
1class Solution(object):
2    def isPalindrome(self, x):
3        # Nếu x là số âm hoặc kết thúc bằng 0 (mà không phải là số 0) thì không phải đối xứng
4        if x < 0 or (x % 10 == 0 and x != 0):
5            return False
6
7        so_dao_nguoc = 0
8        # Chạy vòng lặp để đảo ngược một nửa số x
9        while x > so_dao_nguoc:
10            chu_so_cuoi = x % 10
11            so_dao_nguoc = so_dao_nguoc * 10 + chu_so_cuoi
12            x //= 10
13
14        # Kiểm tra nếu x bằng số đã đảo ngược (cho số chữ số chẵn)
15        # Hoặc x bằng so_dao_nguoc // 10 (cho số chữ số lẻ, bỏ chữ số ở giữa)
16        return x == so_dao_nguoc or x == so_dao_nguoc // 10