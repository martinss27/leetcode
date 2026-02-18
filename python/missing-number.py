# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        expected = n * (n + 1) // 2
        array_sum = sum(nums)

        return expected - array_sum
    
'''in case [3,0,1] is given, the expected sum is 6 (0+1+2+3) and the actual sum is 4 (3+0+1), so the missing number is 2.'''