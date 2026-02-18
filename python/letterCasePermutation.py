# https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        n = len(s)
        s_List = list(s) #converting to list for mutability

        def backtrack(index, current_s_list):
            if index == n:
                result.append("".join(current_s_list))
                return

            backtrack(index + 1, current_s_list)
            
            if current_s_list[index].isalpha():
                original_char = current_s_list[index]

                if current_s_list[index].islower():
                    current_s_list[index] = current_s_list[index].upper()
                else:
                    current_s_list[index] = current_s_list[index].lower()            

        
                backtrack(index + 1, current_s_list)

                current_s_list[index] = original_char

        backtrack(0, s_List)
        return result