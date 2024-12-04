from getinput import getinput

def findXs(array, i, j) -> int:
    sum = 0

    mas1 = array[i-1][j-1] + array[i][j] + array[i+1][j+1]
    mas2 = array[i-1][j+1] + array[i][j] + array[i+1][j-1]

    if(mas1 == "MAS" or mas1[::-1] == "MAS") and (mas2 == "MAS" or mas2[::-1] == "MAS"):
        return 1
    else:
        return 0

sum = 0
wordSearch = getinput(4).split('\n')

if(wordSearch[len(wordSearch) - 1] == ''): wordSearch.pop()

for i in range(1, len(wordSearch) - 1):
    for j in range(1, len(wordSearch[i]) - 1):
        if wordSearch[i][j] == 'A': sum += findXs(wordSearch, i, j)
print(sum)