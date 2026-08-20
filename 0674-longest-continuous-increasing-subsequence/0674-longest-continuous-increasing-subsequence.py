class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        curr_length = 1
        max_length = 1 

        for i in range(1, len(nums)):

            if (nums[i] > nums[i-1]):
                curr_length += 1
            else:
                max_length = max(curr_length,max_length)
                curr_length = 1

        return max(curr_length,max_length)                


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna