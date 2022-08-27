class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res=res+[lst+[i] for lst in res]
        return res
        
