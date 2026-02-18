# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ja_vistos = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in ja_vistos:
                return [ja_vistos[complement], i]
            else:
                ja_vistos[n] = i 