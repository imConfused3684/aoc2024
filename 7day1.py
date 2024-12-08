from getinput import getinput
import operator
from typing import Iterable

opers = { 0 : operator.add, 1 : operator.mul }

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

    for variation in perebor(2, len(line) - 1):
        i = 1
        lineRes = int(line[0])
        for symbol in variation:
            lineRes = opers[symbol](lineRes, int(line[i]))
            i += 1
        if result == lineRes : return result
    return 0

sum = 0
for str in getinput(7).split('\n'):
    if str == '': continue
    sum += checkLine(str.split())
print(sum)