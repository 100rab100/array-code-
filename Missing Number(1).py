class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
        
        
 class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums)
        for i in range(len(nums)):
            res+=(i-nums[i])
        return res    
