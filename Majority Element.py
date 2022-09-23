class Solution:
    def majorityElement(self, num: List[int]) -> int:
        return sorted(num)[int(len(num)/2)]
       
 class Solution:
    def majorityElement(self, num: List[int]) -> int:
        m = {}
        for n in num:
            m[n] = m.get(n, 0) + 1
            if m[n] > len(num)//2:
                return n     
       
    
        
