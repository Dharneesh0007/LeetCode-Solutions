class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        diff = max(nums) - min(nums) - 2 * k
        return max(0, diff)