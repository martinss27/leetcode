# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()

        for idx in range(len(nums)):
            if nums[idx] == idx:
                pass
            elif nums[idx] != idx:
                return idx
            
        return len(nums)