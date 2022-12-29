class Solution:
    def reverse(self, x: int) -> int:
        if x >=0 :
            x=str(x)
            x=x[::-1]
            if int(x)<2147483647:
                return int(x)
            else:
                return 0
            return int(x)
        elif x<0 :
            x=str(-x)
            x=x[::-1]
            if -int(x)>-2147483648:
                return -int(x)
            else:
                return 0
        else:
            return 0
            