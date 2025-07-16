class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        num_rows = len(triangle)
        min_paths = triangle[num_rows-1].copy()

        for r in range(num_rows-2,-1,-1): #inicio do bottom-up
            for c in range(r+1):
                min_paths[c] = min(min_paths[c], min_paths[c + 1]) + triangle[r][c]

        return min_paths[0]