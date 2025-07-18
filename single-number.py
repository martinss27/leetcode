# leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        numeros_unicos = []

        for n in nums:
            if n not in unicos:
                unicos.append(n)
            else:
                unicos.remove(n)

        return unicos.pop()

    #O(n²)