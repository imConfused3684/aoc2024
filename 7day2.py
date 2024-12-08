from getinput import getinput
from typing import Iterable

def perebor(base: int, length: int) -> Iterable[list[int]]:
    for i in range(base**length):
        t = i
        symbols = []
        for j in range(length):
            t = int(t)
            symbols.append(int(t % base))
            t /= base
        yield symbols

def checkLine(line: list[str]) -> int:
    line[0] = line[0][:len(line[0]) - 1]
    result = int(line[0])
    line = line[1:]

    for variation in perebor(3, len(line) - 1):
        i = 1
        lineRes = int(line[0])
        for symbol in variation:
            match symbol:
                case 0:
                    lineRes += int(line[i])
                case 1:
                    lineRes *= int(line[i])
                case 2:
                    lineRes = int(str(lineRes) + str(line[i]))
            i += 1
        if result == lineRes : return result
    return 0

sum = 0
for line in getinput(7).split('\n'):
    if line == '': continue
    sum += checkLine(line.split())
print(sum)