#ONE Ways
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
          return set(range(1, len(nums)+1)) - set(nums)
          
          
# second way
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = [i for i in range(0, len(nums)+1)] # build an array (0, 1, 2, 3, ..., n)
        for i in nums: result[i] = 0 # we index this array, setting "found" elements to zero
        return [i for i in result if i != 0] 
        
        
        
 #Third way
 class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_nums = list(range(1,len(nums)+1))
        res = (set(new_nums) - set(nums))
        return(list(res))
          
