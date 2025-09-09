#https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:

        x = 0
        y = 0

        for char in moves:
            if char == "U":
                y += 1
            if char == "D":
                y -= 1
            if char == "R":
                x += 1
            if char == "L":
                x -= 1
            
        if x == 0 and y == 0:
            return True
        else:
            return False