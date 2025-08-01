class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []

        triangle = [[1]]

        for row_index in range(1, numRows):
            previous_row = triangle[-1]
            current_row = [1]
            
            for indice in range(len(previous_row) - 1):
                value = previous_row[indice] + previous_row[indice + 1]
                current_row.append(value)
                
            current_row.append(1)
            triangle.append(current_row)
        return triangle