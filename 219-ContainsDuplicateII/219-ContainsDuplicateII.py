# Last updated: 5/15/2026, 11:05:07 AM
1class Solution(object):
2    def containsNearbyDuplicate(self, nums, k):
3        # dictionary lưu {giá_trị: chỉ_số_gần_nhất}
4        last_seen = {}
5        for i, num in enumerate(nums):
6            # Nếu số đã xuất hiện và khoảng cách <= k
7            if num in last_seen and i - last_seen[num] <= k:
8                return True
9            last_seen[num] = i 
10        return False