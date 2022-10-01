class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left, right, sum_val, min_len = 0, 0, 0, len(nums) + 1
        while right < len(nums):
            sum_val += nums[right]
            while sum_val >= target:
                min_len = min(right - left + 1, min_len)
                if min_len == 1:
                    return 1
                sum_val -= nums[left]
                left += 1
            right += 1
        return 0 if min_len > len(nums) else min_len
