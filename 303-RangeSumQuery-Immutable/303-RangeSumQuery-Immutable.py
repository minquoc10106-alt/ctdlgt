# Last updated: 5/15/2026, 11:09:27 AM
1class NumArray(object):
2    def __init__(self, nums):
3        # Tạo mảng prefix_sums có độ dài n + 1
4        # prefix_sums[i] lưu tổng của i phần tử đầu tiên
5        self.prefix_sums = [0] * (len(nums) + 1)
6        for i in range(len(nums)):
7            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]
8    def sumRange(self, left, right):
9        # Công thức: Tổng từ left đến right = PrefixSum[right + 1] - PrefixSum[left]
10        return self.prefix_sums[right + 1] - self.prefix_sums[left]