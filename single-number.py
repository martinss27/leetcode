# leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        unicos = set([])

        for n in nums:
            if n not in unicos:
                unicos.add(n)
            else:
                unicos.remove(n)
                
        return unicos.pop()