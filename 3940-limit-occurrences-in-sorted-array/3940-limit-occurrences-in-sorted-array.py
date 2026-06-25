class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        if not nums or k == 0:
            return []
            
        result = []
        current_count = 0
        
        for i in range(len(nums)):
            # If it's the first element or a new distinct number, reset the counter
            if i == 0 or nums[i] != nums[i - 1]:
                current_count = 1
            else:
                current_count += 1
                
            # Only include the element if it hasn't exceeded the limit 'k'
            if current_count <= k:
                result.append(nums[i])
                
        return result      