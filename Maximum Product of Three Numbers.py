class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = sorted(nums)
        n=len(nums)
        return(max(a[n-1] *a[n-2]*a[n-3],a[0]*a[1]*a[n-1]))
