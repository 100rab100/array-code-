class Solution:
    def mySqrt(self, x: int) -> int:
        num = 0
        while x>=num*num: #condition to check 
            num += 1
        return num-1
       #return int(sqrt(x))  # SECOND APPROACH
       #return  int(pow(x,0.5))# THIRD APPROACH
