# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        current_row = [1]

        for row_index in range(1, rowIndex + 1):
            previous_row = current_row
            current_row = [1]

            for indice in range(len(previous_row) - 1):
                value = previous_row[indice] + previous_row[indice + 1]
                current_row.append(value)
                
            current_row.append(1)

        return current_row