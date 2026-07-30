class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        if m * n != r * c:
            return mat
        
        res = [[0] * c for _ in range(r)]
        k = 0
        
        for i in range(m):
            for j in range(n):
                res[k // c][k % c] = mat[i][j]
                k += 1
                
        return res