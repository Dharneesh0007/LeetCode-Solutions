class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        area = 0

        for r in range(n):
            for c in range(n):
                h = grid[r][c]
                if h > 0:
                    area += 2 + 4 * h

                    if r > 0:
                        area -= 2 * min(h, grid[r - 1][c])
                    if c > 0:
                        area -= 2 * min(h, grid[r][c - 1])

        return area