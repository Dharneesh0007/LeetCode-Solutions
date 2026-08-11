class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        S_expected = n * (n + 1) // 2
        S2_expected = n * (n + 1) * (2 * n + 1) // 6
        
        S_actual = sum(nums)
        S2_actual = sum(x * x for x in nums)
        
        diff1 = S_actual - S_expected
        diff2 = S2_actual - S2_expected
        
        sum_dup_miss = diff2 // diff1
        
        duplicate = (diff1 + sum_dup_miss) // 2
        missing = sum_dup_miss - duplicate
        
        return [duplicate, missing]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna