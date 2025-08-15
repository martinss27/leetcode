# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = [] #onde vou guardar os subsets

        def backtrack(index, path):
            result.append(path[:])
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        
        backtrack(0, [])
        return result