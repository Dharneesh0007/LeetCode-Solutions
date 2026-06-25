class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
                if not nums or k == 0:
                    return []
                    
                result = []
                current_count = 0
                
                for i in range(len(nums)):
                
                    if i == 0 or nums[i] != nums[i - 1]:
                        current_count = 1
                    else:
                        current_count += 1
                        
                    if current_count <= k:
                        result.append(nums[i])
                        
                return result      