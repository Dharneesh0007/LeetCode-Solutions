class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        
        for r in range(m):
            for c in range(n):
                total_sum = 0
                count = 0
                
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            total_sum += img[nr][nc] & 0xFF
                            count += 1
                
                smoothed_val = total_sum // count
                img[r][c] |= (smoothed_val << 8)
                
        for r in range(m):
            for c in range(n):
                img[r][c] >>= 8
                
        return img

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna