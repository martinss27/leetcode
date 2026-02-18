# leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/class Solution:
    
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        reversed_nums = [int(str(n)[::-1]) for n in nums]
        combined = nums + reversed_nums

        return len(set(combined))