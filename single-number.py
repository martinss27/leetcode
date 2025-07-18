# leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        numeros_unicos = {}

        for n in nums:
            if n not in numeros_unicos:
                numeros_unicos[n] = 1
            else:
                numeros_unicos[n] += 1

        for num, contagem in numeros_unicos.items():
            if contagem == 1:
                return num

    #O(n)