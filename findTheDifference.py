# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s_list = list(s)
        t_list = list(t)

        for l in s_list:
            if l in t_list:
                t_list.remove(l)

        return t_list.pop()