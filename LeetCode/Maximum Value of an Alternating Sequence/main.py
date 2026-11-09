class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        sub = max(0, (n//2)-1)

        n = (n//2)*2

        return s + (m * n // 2) - sub