a, b = [int(x) for x in input().split()]

def solve(score_a, score_b, cur_depth):
    if score_a%10==6 and score_b%10==7:
        return 0
    
    if cur_depth > 21:
        return 999999
    
    # try a scores
    a = solve(score_a+1, score_b, cur_depth+1)

    # try b scores
    b = solve(score_b+1, score_a, cur_depth+1)

    # return minimum
    return min(a, b) + 1

print(solve(a, b, 0))