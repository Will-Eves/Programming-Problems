class Solution:
    def numberOfWays(self, s: str) -> int:
        # create + init count backwards arrays
        countback0 = []
        countback1 = []

        for i in range(len(s)):
            countback0.append(0)
            countback1.append(0)
        
        countback0[len(s)-1] = s[-1:].count('0')
        countback1[len(s)-1] = s[-1:].count('1')

        # count the number of 1s and 0s backwards for later use
        for i in reversed(range(len(s)-1)):
            c = s[i]

            countback0[i] = countback0[i+1]
            countback1[i] = countback1[i+1]

            if c == '0':
                countback0[i] += 1
            else:
                countback1[i] += 1
        
        # create + init count forwards arrays
        countfor0 = [s[0].count('0')]
        countfor1 = [s[0].count('1')]

        # count the number of 1s and 0s forwards for later use
        for i in range(1, len(s)):
            c = s[i]

            countfor0.append(countfor0[i-1])
            countfor1.append(countfor1[i-1])

            if c == '0':
                countfor0[i] += 1
            else:
                countfor1[i] += 1
        
        # calculate the final number
        total = 0
        for i in range(len(s)):
            if s[i] == '0':
                total += countback1[i] * countfor1[i]
            else:
                total += countback0[i] * countfor0[i]

        return total