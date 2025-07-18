# leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        numeros_unicos = []

        for n in nums:
            if n not in numeros_unicos:
                numeros_unicos.append(n)
            else:
                numeros_unicos.remove(n)

        return numeros_unicos.pop()

    #O(n²)