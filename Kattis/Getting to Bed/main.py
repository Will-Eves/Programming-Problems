n, m, k = [int(x) for x in input().split()]

room = []

for i in range(n):
    room.append([])
    for j in range(m):
        room[i].append(0)

room[0][0] = 1

for i in range(k):
    x, y = [int(x) for x in input().split()]
    
    room[x][y] = -1

bx, by = [int(x) for x in input().split()]

for i in range(100):
    for x in range(n):
        for y in range(m):
            if room[x][y] != -1:
                if x != 0 and room[x-1][y] > room[x][y]:
                    room[x][y] += 1
                if x != n-1 and room[x+1][y] > room[x][y]:
                    room[x][y] += 1
                if y != 0 and room[x][y-1] > room[x][y]:
                    room[x][y] += 1
                if y != m-1 and room[x][y+1] > room[x][y]:
                    room[x][y] += 1

if room[bx][by] > 0:
    print('SLEEPING')
else:
    print('IMPOSSIBLE')