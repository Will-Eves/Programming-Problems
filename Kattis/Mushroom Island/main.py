import math

n = int(input())
points = []

possible = []

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

#load
for i in range(n):
    x, y = map(int, input().split())

    points.append([i+1,x,y])
    possible.append(i)

# if dist < 10000
#   add to not possible
#   add to all
# else
#   add to possible
#   add to all
# for p in possible
#  check

for p in possible:
    if p == -1:
        continue
    
    point1 = points[p]

    good = True

    for point2 in points:
        if point1[0] == point2[0]:
            continue
        
        dist = distance(point1[1], point1[2], point2[1], point2[2])

        if dist < 10000:
            # remove point1 and point2 from possible
            possible[point1[0]-1] = -1
            possible[point2[0]-1] = -1
            good = False
    
    if good:
        print(point1[0])
        break