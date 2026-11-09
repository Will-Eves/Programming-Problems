class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occ = []

        # determine the occurances of x
        for i in range(len(nums)):
            if nums[i] == x:
                occ.append(i)
        
        out = []

        for q in queries:
            if q > len(occ):
                out.append(-1)
            else:
                out.append(occ[q-1])
        
        return out