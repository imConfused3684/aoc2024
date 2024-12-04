from getinput import getinput

def findWords(array, i, j, max_i, max_j) -> int:
    sum = 0
    u = i >= 3
    d = max_i - i > 3
    l = j >= 3
    r = max_j - j > 3

    if(u):
        if(array[i][j] + array[i-1][j] + array[i-2][j]  + array[i-3][j] == "XMAS"): sum += 1
    if(d):
        if(array[i][j] + array[i+1][j] + array[i+2][j]  + array[i+3][j] == "XMAS"): sum += 1

    if(l):
        if(array[i][j] + array[i][j-1] + array[i][j-2]  + array[i][j-3] == "XMAS"): sum += 1
    if(r):
        if(array[i][j] + array[i][j+1] + array[i][j+2]  + array[i][j+3] == "XMAS"): sum += 1

    if(u and r):
        if(array[i][j] + array[i-1][j+1] + array[i-2][j+2]  + array[i-3][j+3] == "XMAS"): sum += 1
    if(u and l):
        if(array[i][j] + array[i-1][j-1] + array[i-2][j-2]  + array[i-3][j-3] == "XMAS"): sum += 1
    if(d and r):
        if(array[i][j] + array[i+1][j+1] + array[i+2][j+2]  + array[i+3][j+3] == "XMAS"): sum += 1
    if(d and l):
        if(array[i][j] + array[i+1][j-1] + array[i+2][j-2]  + array[i+3][j-3] == "XMAS"): sum += 1
    

    return sum

sum = 0
wordSearch = getinput(4).split('\n')

if(wordSearch[len(wordSearch) - 1] == ''): wordSearch.pop()

for i in range(len(wordSearch)):
    for j in range(len(wordSearch[i])):
        if wordSearch[i][j] == 'X': sum += findWords(wordSearch, i, j, len(wordSearch), len(wordSearch[i]))
print(sum)

print("X" + "M" + "A" + "S" == "XMAS")
