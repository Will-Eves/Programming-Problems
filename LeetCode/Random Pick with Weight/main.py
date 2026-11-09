import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.t = sum(w)

    def pickIndex(self) -> int:
        v = random.random() * self.t
        
        i = 0
        index = 0
        while index < len(self.w):
            v -= self.w[index]

            if v <= 0:
                return index
            
            index += 1
        
        return -1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()