class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
            
            
            
            # Approach 2
            
           
    def searchInsert( nums: List[int], target: int) -> int:
         return sorted(nums + [target]).index(target)
