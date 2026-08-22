class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_seen = {}
        counts = {}
        
        degree = 0
        min_length = 0
        
        for i, num in enumerate(nums):
            if num not in first_seen:
                first_seen[num] = i
                
            counts[num] = counts.get(num, 0) + 1
            
            if counts[num] > degree:
                degree = counts[num]
                min_length = i - first_seen[num] + 1
            elif counts[num] == degree:
                min_length = min(min_length, i - first_seen[num] + 1)
                
        return min_length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna