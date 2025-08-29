# https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s_counts = {}

        for char in s:
            if char not in s_counts:
                s_counts[char] = 1
            else:
                s_counts[char] += 1

        for char in t:
            if char not in s_counts or s_counts[char ] == 0:
                return char

            else:
                s_counts[char] -= 1