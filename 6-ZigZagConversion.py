class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 0:
            return ''
        if numRows ==1:
            return s
        else:
            zig = []
            for i in range(numRows):
                zig.append([])
            n=0
            j=0
            for i in s:
                if j == 0:
                    zig[n].append(i)
                    n+=1
                    if n == numRows-1:
                        j=1
                elif j == 1:
                    zig[n].append(i)
                    n-=1
                    if n == 0:
                        j = 0
            z = ''
            for i in zig:
                for j in i:
                    z+=j
            return str(z)