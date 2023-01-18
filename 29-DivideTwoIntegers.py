class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==0:return 0
        if divisor==1:return dividend
        if divisor==-1: 
            if -dividend<-(2**31): return -(2**31)
            elif -dividend>2**31-1: return 2**31-1
            else:return -dividend
        if (divisor<0 and dividend<0) or (dividend>0 and divisor>0):
            return dividend//divisor
        if dividend%divisor==0:return dividend//divisor
        return dividend//divisor+1
            