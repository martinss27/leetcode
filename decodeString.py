# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        current_string = ""
        current_number = 0

        for char in s:
            if char.isdigit():
                current_number = (current_number * 10) + int(char)
            
            elif char == '[':

                stack.append(current_number)
                stack.append(current_string)

                current_number = 0
                current_string = ""
            
            elif char == "]":
                saved_string = stack.pop()
                repeat_count = stack.pop()

                current_string = saved_string + (current_string * repeat_count)

            else:
                current_string += char

        
        return current_string