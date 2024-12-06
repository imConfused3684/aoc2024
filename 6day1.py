from getinput import getinput
from typing import Dict


def getCords(array: list[str]) -> tuple[Dict[int, list[int]], tuple[int, int]]:
    obstructions = {}
    for i in range (len(array)):
        obstructions[i] = []
        for j in range(len(array[i])):
            if array[i][j] == '#': obstructions[i].append(j)
            if array[i][j] == '^': guard = (int(i), int(j))
    return (obstructions, guard)

def changeToX(string: str, position: int) -> str:
    if(position == 0): return 'X' + string[1:]
    elif(position == len(string) - 1): return string[:position] + 'X'
    else: return string[:position] + 'X' + string[position + 1:]

def drawX(start: tuple[int, int], end: tuple[int, int], facing: int, map: list[str]):
    match facing:
        case 0:
            if end : end_position = end[0]+1
            else: end_position = 0
            for i in range(end_position, start[0]+1): map[i] = changeToX(map[i], start[1])
        case 1:
            if end : end_position = end[1]
            else: end_position = len(map[start[0]])
            for i in range(start[1], end_position): map[start[0]] = changeToX(map[start[0]], i)            
        case 2:
            if end : end_position = end[0]
            else: end_position = len(map)
            for i in range(start[0]+1, end_position): map[i] = changeToX(map[i], start[1])           
        case 3:
            if end : end_position = end[1]+1
            else: end_position = 0
            for i in range(end_position, start[1]): map[start[0]] = changeToX(map[start[0]], i)  

def isobstraction(position: tuple[int, int], obstructions: Dict[int, list[int]], facing: int) -> tuple[int, int]:
    match facing:
        case 0:
            for i in reversed(range(position[0])):
                if position[1] in obstructions[i]: return (i,position[1])
            return ()
        case 1:
            for i in obstructions[position[0]]: 
                if i > position[1]: return (position[0],i)
            return ()
        case 2:
            for i in range(position[0] + 1, len(obstructions)):
                if position[1] in obstructions[i]: return (i,position[1])
            return ()
        case 3:
            for i in reversed(obstructions[position[0]]): 
                if i < position[1]: return (position[0],i)
            return ()


map = getinput(6).split('\n')
if(map[-1] == ''): map.pop()
navigation = getCords(map)

# 0 - up, 1 - rigth, 2 - down, 3 - left
facing = 0
position = navigation[1]
obstractions = navigation[0]
flag = True
while flag:
    match facing:
        case 0:
            obstraction = isobstraction(position, obstractions, 0)
            drawX(position, obstraction, 0, map)
            if obstraction:
                position = (obstraction[0]+1,obstraction[1])
                facing = 1
            else:
                flag = False
        case 1:
            obstraction = isobstraction(position, obstractions, 1)
            drawX(position, obstraction, 1, map)
            if obstraction:
                position = (obstraction[0],obstraction[1]-1)
                facing = 2
            else:
                flag = False
        case 2:
            obstraction = isobstraction(position, obstractions, 2)
            drawX(position, obstraction, 2, map)
            if obstraction:
                position = (obstraction[0]-1,obstraction[1])
                facing = 3
            else:
                flag = False
        case 3:
            obstraction = isobstraction(position, obstractions, 3)
            drawX(position, obstraction, 3, map)
            if obstraction:
                position = (obstraction[0],obstraction[1]+1)
                facing = 0
            else:
                flag = False

sum = 0
file = open('output', 'w')
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 'X': sum += 1
    file.write(map[i] + '\n')
file.close()
print(sum)