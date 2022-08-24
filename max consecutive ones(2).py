#Approach one
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = result = 0
        for n in nums:
            consecutive = consecutive*n+n
            result = max(result, consecutive)
        return result
  
  # Approach 2
  class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c1,c2=0,0
        for i in nums:
            if i==1:
                c1+=1
            elif i==0:
                c1=0
            if c1>c2:
                c2=c1
        return c2
