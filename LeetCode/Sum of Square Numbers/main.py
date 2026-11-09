import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = int(math.sqrt(c))
        
        b = 0
        while a >= b:
            while a*a + b*b < c:
                b += 1
        
            if a*a + b*b == c:
                return True
            
            a -= 1
        
        return False