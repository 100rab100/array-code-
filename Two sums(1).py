class Solution(object):
   def twoSum(self, nums, target):
        for i in range(len(nums)):
            

            for j in range(i + 1, len(nums)):
                
                if target == nums[i] + nums[j]:
                    
                    return ([i,j])
                    break
            
            
            

 
    def twoSum(self, nums, target):
      
        dic = {}
        for i, n in enumerate(nums): 
            
            if n in dic:
                
                return [dic[n], i]
            dic[target-n] = i
