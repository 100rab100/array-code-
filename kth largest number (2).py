#FRIST approach 
# O(nlgn) time
def findKthLargest1(nums, k):
    return sorted(nums, reverse=True)[k-1]
    
#SECOND approach
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(k):
            ans = max(nums)
            nums.remove(ans)
            
        return ans
        
        
#THIRD APPROACH 
def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
    
