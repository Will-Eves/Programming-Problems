class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = set(nums)
        dlen = len(distinct)

        n = len(nums)

        count = 0

        for i in range(n):
            curr = set()

            for j in range(i, n):
                curr.add(nums[j])
            
                if len(curr) == dlen:
                    count += 1
        
        return count