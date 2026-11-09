n, c1, c2, c3 = map(int, input().split())

def min_distance(a, b, n):
    return min(abs(a-b), n-abs(a-b))

dist_c1_c2 = min_distance(c1, c2, n)
dist_c2_c3 = min_distance(c2, c3, n)
dist_c1_c3 = min_distance(c1, c3, n)

min_dist = min(dist_c1_c2, dist_c2_c3, dist_c1_c3)
max_dist = max(dist_c1_c2, dist_c2_c3, dist_c1_c3)

def days_after_launch(dist, x):
    return abs(dist - x)

def calc_min_days(x):
    global dist_c1_c2
    global dist_c2_c3
    global dist_c1_c3

    days_c1_c2 = days_after_launch(dist_c1_c2, x)
    days_c2_c3 = days_after_launch(dist_c2_c3, x)
    days_c1_c3 = days_after_launch(dist_c1_c3, x)

    return max(days_c1_c2, days_c2_c3, days_c1_c3)

min_days = 9999999999999999999999999999

while max_dist-min_dist > 20:
    spread = (max_dist-min_dist)//min(20, max_dist-min_dist)

    calculations = []

    # calculate stuff
    i = min_dist
    while i <= max_dist:
        calculations.append([i, calc_min_days(i)])

        i += spread
    
    # calculate last
    if calculations[len(calculations)-1][0] != max_dist:
        calculations.append([max_dist, calc_min_days(max_dist)])
    
    # now determine where its like this: V
    # then made min_dist at the start of the V
    # and make max_dist at the end of the V
    best = calculations[0][1]
    best_index = 0

    for j in range(len(calculations)):
        if calculations[j][1] < best:
            best = calculations[j][1]
            best_index = j
    
    min_days = best

    left = calculations[max(best_index-1, 0)][0]
    right = calculations[min(best_index+1, len(calculations))][0]

    min_dist = left
    max_dist = right
    
    if spread < 20:
        break

for i in range(min_dist, max_dist+1):
    days = calc_min_days(i)

    if days < min_days:
        min_days = days

print(min_days)