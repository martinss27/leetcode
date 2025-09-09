#https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:

        vertical_return = moves.count("U") == moves.count("D")

        horizontal_return = moves.count("R") == moves.count("L")

        return vertical_return and horizontal_return
    
# using count to count the number of moves in each direction and check if they are equal for opposite directions(U-D and R-L)