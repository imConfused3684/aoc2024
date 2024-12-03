from getinput import getinput
import re

sum = 0
regexp = r"mul\(([0-9]+,[0-9]+)\)"
for str in re.findall(regexp, getinput(3)):
    sum += int(str.split(',')[0]) * int(str.split(',')[1])
print(sum)