from getinput import getinput

def find9s(previous: str, curr_i: int, curr_j: int, map: list[list[str]], found9s: list[tuple[int, int]]) -> int:
    if(map[curr_i][curr_j] == '9'):
        if(not (curr_i, curr_j) in found9s): found9s.append((curr_i, curr_j)); return 1
        else: return 0

    sum = 0

    if previous != 'u' and curr_i > 0 and int(map[curr_i-1][curr_j]) - int(map[curr_i][curr_j]) == 1: sum += find9s('d', curr_i-1, curr_j, map, found9s)

    if previous != 'r' and curr_j < len(map[0]) - 1 and int(map[curr_i][curr_j+1]) - int(map[curr_i][curr_j]) == 1: sum += find9s('l', curr_i, curr_j+1, map, found9s)

    if previous != 'd' and curr_i < len(map) - 1 and int(map[curr_i+1][curr_j]) - int(map[curr_i][curr_j]) == 1: sum += find9s('u', curr_i+1, curr_j, map, found9s)

    if previous != 'l' and curr_j > 0 and int(map[curr_i][curr_j-1]) - int(map[curr_i][curr_j]) == 1: sum += find9s('r', curr_i, curr_j-1, map, found9s)

    return sum
        
map = getinput(10).split('\n')
if map[-1] == '': map.pop()

score = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        found9s = []
        if map[i][j] == '0': score += find9s('', i, j, map, found9s)
print(score)