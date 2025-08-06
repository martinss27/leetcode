# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = []
        nums2_set = set(nums2)

        for n in nums1:
            if n in nums2_set and n not in result:
                result.append(n)
        return result
    
# o(n)