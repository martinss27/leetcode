# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        num_elementos = len(nums)
        total_subconjuntos = 2**num_elementos  
        result = []  

        for mask_number in range(total_subconjuntos):
            
            subset_atual = []

            for element_index in range(num_elementos):

                if (mask_number >> element_index) & 1:
                    
                    subset_atual.append(nums[element_index])
            
            result.append(subset_atual)
            
        return result