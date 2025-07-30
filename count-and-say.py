# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        def get_next_term(s):
            res = []
            count = 1

            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                else:
                    count_as_str = str(count)
                    res.append(count_as_str)
                    res.append(s[i-1])
                    count = 1

            res.append(str(count))
            res.append(s[-1])
            return ''.join(res)

            
        resultado = "1" 
        for _ in range(n -1): 
            resultado = get_next_term(resultado)
        return resultado