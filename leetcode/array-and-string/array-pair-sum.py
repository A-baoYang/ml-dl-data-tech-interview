class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        min_sum = 0
        for i in range(len(nums) // 2):
            min_sum += min(nums[i * 2 : (i + 1) * 2])
        return min_sum
