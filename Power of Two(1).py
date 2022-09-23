#ONE way
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
    
        if n < 1:
            
            return False
    
        return self.isPowerOfTwo(n/2)
#TWO wayclass Solution:
   def isPowerOfTwo(self, n: int) -> bool:
        if (n<=0):
            return False
        return n&(n-1)==0
