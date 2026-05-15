# Last updated: 5/15/2026, 9:51:26 AM
1class Solution(object):
2    def threeSumClosest(self, nums, target):
3        nums.sort()
4        n = len(nums)
5        closest_sum = float('inf')  
6        for i in range(n - 2):
7            # Bỏ qua các số trùng lặp để tối ưu
8            if i > 0 and nums[i] == nums[i-1]:
9                continue
10            l, r = i + 1, n - 1
11            while l < r:
12                current_sum = nums[i] + nums[l] + nums[r]
13                if current_sum == target:
14                    return current_sum             
15                # Cập nhật kết quả gần nhất
16                if abs(current_sum - target) < abs(closest_sum - target):
17                    closest_sum = current_sum               
18                if current_sum < target:
19                    l += 1
20                else:
21                    r -= 1                    
22        return closest_sum