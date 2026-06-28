class Solution(object):
    def twoSum(self, nums, target):
       seen_nums={}

       for i,num in enumerate(nums):
         complement= target - num
         if complement in seen_nums:
           return [seen_nums[complement],i]
         else:
            seen_nums[num]=i

        