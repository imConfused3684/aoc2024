from typing import Dict
from getinput import getinput

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
                    an1_x = 2*antenna[0] - x
                    an1_y = 2*antenna[1] - y
                    if(0 <= an1_x < x_max) and (0 <= an1_y < y_max) and (not (an1_x, an1_y) in antinodeDict): antinodeDict.append((an1_x, an1_y))
                    
                    an2_x = 2*x - antenna[0]
                    an2_y = 2*y - antenna[1]
                    if(0 <= an2_x < x_max) and (0 <= an2_y < y_max) and (not (an2_x, an2_y) in antinodeDict): antinodeDict.append((an2_x, an2_y))
                
                antennaDict[map[x][y]].append((x,y))

print(len(antinodeDict))
            