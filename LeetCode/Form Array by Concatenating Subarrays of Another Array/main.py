class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        cur = 0
        curl = len(groups[cur])
        gindex = 0

        lm = 0

        valid = False

        i = 0
        while i < len(nums):
            n = nums[i]

            print(n)
            print(groups[cur][gindex])

            if n == groups[cur][gindex]:
                gindex += 1

                if gindex == curl:
                    cur += 1

                    if cur == len(groups):
                        valid = True
                        break

                    curl = len(groups[cur])
                    gindex = 0

                    lm = i
                
                i += 1
            else:
                gindex = 0

                i = lm + 1
                lm += 1
    
        return valid