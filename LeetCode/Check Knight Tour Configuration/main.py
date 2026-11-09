class Solution:
    def checkValidGrid(self, grid: list[list[int]]) -> bool:
        moves = [-1] * (len(grid) * len(grid))

        for i in range(len(grid)):
            for j in range(len(grid)):
                v = grid[i][j]

                moves[v] = [i, j]
        
        if not moves[0] == [0, 0]:
            return False

        last = moves[0]

        valid = True

        for i in range(1, len(moves)):
            # determine if valid
            cur = moves[i]

            iabs = abs(last[0] - cur[0])
            jabs = abs(last[1] - cur[1])

            last = cur

            if iabs == 1 and jabs == 2 or iabs == 2 and jabs == 1:
                continue
            else:
                valid = False
                break
        
        return valid