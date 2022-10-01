class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        collect_a, collect_b, set_num = {}, {}, 0
        for i in nums1:
            for j in nums2:
                if i + j in collect_a:
                    collect_a[i + j] += 1
                else:
                    collect_a[i + j] = 1
        for k in nums3:
            for l in nums4:
                if 0 - (k + l) in collect_a:
                    if k + l in collect_b:
                        collect_b[k + l] += 1
                    else:
                        collect_b[k + l] = 1
        print(collect_a, collect_b)
        for i in collect_b:
            set_num += collect_a[-i] * collect_b[i]
        return set_num
