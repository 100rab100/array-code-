class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:  
        return [i for i in nums if i % 2 ==0]+[i for i in nums if i % 2 != 0]
    
    
    
    #2
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:  
        if len(nums) == 1: return nums
        l = []
        for i in nums:
            l.insert(0,i) if i % 2 == 0 else l.append(i)
        return l  
