# first approach
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort( reverse = True )
        
        return nums[k-1]
      
#2 approach

def findKthLargest(nums: list[int], k: int) -> int:
    ans = 0
    for i in range(k):
        ans = max(nums)
        nums.remove(ans)

    return ans

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums,k))

#Output: 5
