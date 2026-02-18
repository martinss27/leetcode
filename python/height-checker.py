# https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        expected = sorted(heights)
        
        mismatches = sum(height != exp_height 
                        for height, exp_height 
                        in zip(heights, expected))

        return mismatches