class Solution:
    def lengthOfLastWord(self, s: str) -> int:
          
        pointer = len(s) - 1

        while pointer >= 0 and s[pointer] == " ": # find the last non-space character
            pointer = pointer - 1
        
        length = 0

        while pointer >= 0 and s[pointer] != " ": # count the length of the last word
            length = length + 1
            pointer = pointer - 1

        
        return length