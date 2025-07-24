# https://leetcode.com/problems/3sum/description/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() # sort the array to use two pointers technique
        triplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i -1]:
                    continue # skip duplicates for the 1st element

            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
            
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    # found a valid triplet
                    triplets.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  

                    left += 1
                    right -= 1
        
        return triplets