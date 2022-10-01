class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sp, ep = 0, len(numbers) - 1
        while numbers[sp] + numbers[ep] != target:
            if numbers[sp] + numbers[ep] > target:
                ep -= 1
            else:
                sp += 1

        return [sp + 1, ep + 1]
