#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        insert_pos = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[insert_pos] = nums[i]
                insert_pospos += 1

        return insert_pos