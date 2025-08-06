# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        seen = set()
        nums2_set = set(nums2)

        for n in nums1:
            if n in nums2_set and n not in seen:
                result.append(n)
                seen.add(n)
        return result
    
# o(1)