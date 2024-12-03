from getinput import getinput
import re

sum = 0
mulOn = 1

regexp = r"mul\(([0-9]+,[0-9]+)\)|(do\(\))|(don't\(\))"
for tup in re.findall(regexp, getinput(3)):
    for result in tup:
        if(result == 'do()'):
            mulOn = 1
        elif(result == 'don\'t()'):
            mulOn = 0
        elif(result != ''):
            sum += int(result.split(',')[0]) * int(result.split(',')[1]) * mulOn
print(sum)