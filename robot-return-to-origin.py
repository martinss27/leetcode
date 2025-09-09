#https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:

        x = 0
        y = 0

        for char in moves:
            if char == "U":
                y += 1
            elif char == "D":
                y -= 1
            elif char == "R":
                x += 1
            elif char == "L":
                x -= 1
            
        return x == 0 and y == 0
    
# sligthly faster solution, because it avoids multiple 'if' checks
# return simplified to a single line