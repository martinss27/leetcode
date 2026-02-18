# leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        def backtrack(path, atual):
            if len(path) ==  len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if atual[i]:
                    continue
                if i > 0 and nums[i] == nums[i -1] and not atual[i - 1]:
                    continue

                atual[i] = True
                path.append(nums[i])
                backtrack(path, atual)
                path.pop()
                atual[i] = False

        backtrack([], [False] * len(nums))
        return result