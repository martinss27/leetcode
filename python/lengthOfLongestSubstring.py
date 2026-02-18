# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_length = 0
        current_substring = ""

        for char in s:
            while char in current_substring:
                current_substring = current_substring[1:]
            
            current_substring += char
            max_length = max(max_length, len(current_substring))            

        return max_length
