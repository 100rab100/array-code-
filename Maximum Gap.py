class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        maxgap = 0
        for i in range(1, len(nums)):
            maxgap = max(maxgap, nums[i] - nums[i -1])
        return maxgap
        
