from getinput import getinput

pairs = getinput(1).split('\n')
left, right = [], []

for pair in pairs:
    nums = pair.split("   ")
    if(len(nums) != 2):
        continue
    left.append(int(nums[0]))
    right.append(int(nums[1]))

left.sort()
right.sort()
sum = 0

for i in range(len(pairs) - 1):
    sum += abs(left[i] - right[i])

print(sum)
