from typing import Dict, Iterable
from getinput import getinput

def nodeY(nodeX: int, x1: int, y1: int, x2: int, y2: int)-> int:
    return nodeX*(y2 - y1)/(x2 - x1) + y1 - x1*(y2 - y1)/(x2 - x1)

def findNodes(x1: int, y1: int, x2: int, y2: int, x_max: int, y_max: int) -> Iterable[tuple[int, int]]:
    if(x1 == x2):
        for i in range(y_max):
            yield (x1, i)
    else:
        for i in range(x_max):
            nY = nodeY(i, x1, y1, x2, y2)
            if round(nY, 5).is_integer(): yield (i, int(round(nY, 1)))

map = getinput(8).split('\n')
if(map[-1] == ''): map.pop()

x_max = len(map[0])
y_max = len(map)

antennaDict: Dict[str, list[tuple[int,int]]] = {}
antinodeDict: list[tuple[int,int]] = []

for y in range(y_max):
    for x in range(x_max):
        if map[x][y] != '.':
            if not map[x][y] in antennaDict:
                antennaDict[map[x][y]] = [(x,y)]
            else:
                for antenna in antennaDict[map[x][y]]:
                    for node in findNodes(x, y, antenna[0], antenna[1], x_max, y_max):
                        if(0 <= node[0] < x_max) and (0 <= node[1] < y_max) and (not node in antinodeDict): antinodeDict.append(node)
                antennaDict[map[x][y]].append((x,y))
print(len(antinodeDict))
            