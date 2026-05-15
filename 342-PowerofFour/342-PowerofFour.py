# Last updated: 5/15/2026, 11:10:16 AM
1class Solution(object):
2    def isPowerOfFour(self, n):
3        # Điều kiện 1: n phải dương
4        # Điều kiện 2: n phải là lũy thừa của 2 (n & (n-1) == 0)
5        # Điều kiện 3: n % 3 == 1 (mẹo toán học thay cho việc kiểm tra vị trí bit)
6        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1