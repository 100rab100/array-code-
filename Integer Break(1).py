class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        if n%3 == 0:
            return int(3**(n/3))
        elif n%3 == 1: 
            return int(3**(n//3)/3*2*2)
        else:
            return int(3**(n//3)*2)
        
        
