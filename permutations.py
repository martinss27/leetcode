#  leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(path, current):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if not current[i]:
                    current[i] = True
                    path.append(nums[i])

                    backtrack(path,current)

                    path.pop()
                    current[i] = False
                    
        backtrack([], [False] * len(nums))
        return result