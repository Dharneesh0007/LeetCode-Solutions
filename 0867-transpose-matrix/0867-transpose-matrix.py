class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        R = len(matrix)
        C = len(matrix[0])
        
        transposed = [[0] * R for _ in range(C)]
        
        for r in range(R):
            for c in range(C):
                transposed[c][r] = matrix[r][c]
                
        return transposed