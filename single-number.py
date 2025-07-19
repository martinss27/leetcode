class Solution:    
    def singleNumber(self, nums: List[int]) -> int:

        resultado = 0

        for n in nums:
            resultado ^= n
        return resultado
