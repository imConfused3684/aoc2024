from getinput import getinput

pairs = getinput(1).split('\n')
left, right = {}, []

for pair in pairs:
    nums = pair.split("   ")
    if(len(nums) != 2):
        break
    ln = int(nums[0])
    if ln in left:
        left[ln][0] += 1
    else:
        left[ln] = [1,0]
    right.append(int(nums[1]))

for n in right:
    if n in left:
        left[n][1] += n

sum = 0
for n in left:
    sum += left[n][0]*left[n][1]

print(sum)

