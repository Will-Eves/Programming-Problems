def longest(nums, greater):
    temp = nums[0]
    longest = 1
    for i in range(len(nums)):
        if greater and temp < nums[i]:
            greater = not greater
            longest += 1
            temp = nums[i]
        elif not greater and temp > nums[i]:
            greater = not greater
            longest += 1
            temp = nums[i]
        else:
            temp = nums[i]
    return longest

n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

print(max(longest(arr, False), longest(arr, True)))