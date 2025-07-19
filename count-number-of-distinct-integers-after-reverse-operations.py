# leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/class Solution:
    class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        reversed_list = []

        for n in nums:
            reverso = int(str(n)[::-1])
            reversed_list.append(reverso)
        
        todos = nums + reversed_list
        apenas_nums_unicos = len(set(todos))

        return apenas_nums_unicos