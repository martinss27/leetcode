# https://leetcode.com/problems/find-the-difference/
from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s_counts = Counter(s)
        t_counts = Counter(t)

        result = (t_counts - s_counts)

        return list(result.keys())[0]