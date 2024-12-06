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

def isobstraction(position: tuple[int, int], obstructions: Dict[int, list[int]], facing: int) -> tuple[int, int]:
    match facing:
        case 0:
            for i in reversed(range(position[0])):
                if position[1] in obstructions[i]: return (i,position[1])
            return ()
        case 1:
            if(position[0] >= len(obstructions) or position[0] == -1): return ()
            for i in obstructions[position[0]]: 
                if i > position[1]: return (position[0],i)
            return ()
        case 2:
            for i in range(position[0] + 1, len(obstructions)):
                if position[1] in obstructions[i]: return (i,position[1])
            return ()
        case 3:
            if(position[0] >= len(obstructions) or position[0] == -1): return ()
            for i in reversed(obstructions[position[0]]): 
                if i < position[1]: return (position[0],i)
            return ()

def checkup(position: tuple[int, int], obstructions: Dict[int, list[int]]) -> bool:
    pos1 = isobstraction((position[0]-1, position[1]), obstructions, 3) 
    if(not pos1): return False
    pos2 = isobstraction((pos1[0], pos1[1]+1), obstructions, 0)
    if(not pos2): return False
    pos3 = isobstraction((pos2[0]+1, pos2[1]), obstructions, 1)
    if(not pos3): return False
    pos4 = isobstraction((pos3[0], pos3[1]-1), obstructions, 2)
    if(not pos3[1]-1 == position[1]): return False
    return (not pos4) or (pos4[1] == position[1] and pos4[0] > position[0])
def checkright(position: tuple[int, int], obstructions: Dict[int, list[int]]) -> bool:
    pos1 = isobstraction((position[0], position[1]+1), obstructions, 0) 
    if(not pos1): return False
    pos2 = isobstraction((pos1[0]+1, pos1[1]), obstructions, 1)
    if(not pos2): return False
    pos3 = isobstraction((pos2[0], pos2[1]-1), obstructions, 2)
    if(not pos3): return False
    pos4 = isobstraction((pos3[0]-1, pos3[1]), obstructions, 3)
    if(not pos3[0]-1 == position[0]): return False
    return (not pos4) or (pos4[0] == position[0] and pos4[1] < position[1])
def checkdown(position: tuple[int, int], obstructions: Dict[int, list[int]]) -> bool:
    pos1 = isobstraction((position[0]+1, position[1]), obstructions, 1) 
    if(not pos1): return False
    pos2 = isobstraction((pos1[0], pos1[1]-1), obstructions, 2)
    if(not pos2): return False
    pos3 = isobstraction((pos2[0]-1, pos2[1]), obstructions, 3)
    if(not pos3): return False
    pos4 = isobstraction((pos3[0], pos3[1]+1), obstructions, 0)
    if(not pos3[1]+1 == position[1]): return False
    return (not pos4) or (pos4[1] == position[1] and pos4[0] < position[0])
def checkleft(position: tuple[int, int], obstructions: Dict[int, list[int]]) -> bool:
    pos1 = isobstraction((position[0], position[1]-1), obstructions, 2) 
    if(not pos1): return False
    pos2 = isobstraction((pos1[0]-1, pos1[1]), obstructions, 3)
    if(not pos2): return False
    pos3 = isobstraction((pos2[0], pos2[1]+1), obstructions, 0)
    if(not pos3): return False
    pos4 = isobstraction((pos3[0]+1, pos3[1]), obstructions, 1)
    if(not pos3[0]+1 == position[0]): return False
    return (not pos4) or (pos4[0] == position[0] and pos4[1] > position[1])


map = getinput(0).split('\n')
if(map[-1] == ''): map.pop()
navigation = getCords(map)

# 0 - up, 1 - rigth, 2 - down, 3 - left


sum = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if (checkup((i,j), navigation[0]) or checkright((i,j), navigation[0]) or checkdown((i,j), navigation[0]) or checkleft((i,j), navigation[0])): sum += 1
print(sum) # That's not the right answer; your answer is too low