class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        inters = set(nums1) & set(nums2)
        nums1, nums2 = [c for c in nums1 if c in inters], [
            c for c in nums2 if c in inters
        ]
        if len(nums1) <= len(nums2):
            nums = nums1.copy()
        else:
            nums = nums2.copy()
        outputs = []
        for c in nums:
            if c in nums1 and c in nums2:
                outputs.append(c)
                nums1.remove(c)
                nums2.remove(c)
        return outputs
