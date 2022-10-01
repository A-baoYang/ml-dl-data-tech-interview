class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast, val in enumerate(nums):
            if val:
                nums[slow] = nums[fast]
                slow += 1
        for z in range(slow, len(nums)):
            nums[z] = 0
        return nums
