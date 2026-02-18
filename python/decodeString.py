class Solution:
    def decodeString(self, s: str) -> str:
        # We use a global index or pass the index by reference/as a list
        # to keep track of our position in the string across recursive calls.
        self.index = 0

        def solve():
            result = []
            current_number = 0
            
            while self.index < len(s):
                char = s[self.index]
                self.index += 1

                if char.isdigit():
                    current_number = current_number * 10 + int(char)
                elif char == '[':
                    # Recursively solve the inner part
                    inner_string = solve()
                    result.append(inner_string * current_number)
                    current_number = 0
                elif char == ']':
                    # End of the current level, return the result
                    return "".join(result)
                else:
                    # It's a letter
                    result.append(char)
            
            return "".join(result)

        return solve()

