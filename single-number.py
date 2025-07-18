# leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        unicos = set([])

        for n in nums:
            unicos.remove(n) if n in unicos else unicos.add(n) 
                
        return unicos.pop()