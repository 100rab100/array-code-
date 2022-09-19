class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int):
        
        result = []
        for i in nums1:
            for x in nums2:
                result.append([i,x])
        return sorted(result,key= sum)[0:k]
        
        
        
        # ALL TEST CASES ARE NOT PASSED 
        
