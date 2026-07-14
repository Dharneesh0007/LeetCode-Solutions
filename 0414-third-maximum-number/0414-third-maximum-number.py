class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_max = float('-inf')
        second_max = float('-inf')
        third_max = float('-inf')
        
        for num in nums:
            if num == first_max or num == second_max or num == third_max:
                continue
            
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max:
                third_max = second_max
                second_max = num
            elif num > third_max:
                third_max = num
                
        if third_max == float('-inf'):
            return first_max
            
        return third_max