class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            desk_index = abs(nums[i]) - 1
            nums[desk_index] = -abs(nums[desk_index])
            
        missing_numbers = []
        for i in range(len(nums)):
            if nums[i] > 0:
                missing_numbers.append(i + 1)
                
        return missing_numbers