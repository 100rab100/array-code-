#ONE way
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        for i in nums1:
            if i in dict1:
                dict1[i] +=1
            else:
                dict1[i] = 1
        res = []
        for i in nums2:
            if i in dict1 and dict1[i]>0:
                res.append(i)
                dict1[i] -=1
        return res
        
