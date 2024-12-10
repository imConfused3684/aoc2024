from getinput import getinput

filesystem = getinput(9).split('\n')
filesystem = filesystem[0]

fileline: list[str] = []
id = 0
for i in range(len(filesystem)):
    if i % 2 == 0:
        for j in range(int(filesystem[i])):
            for symbol in str(id):
                fileline.append(symbol)
        id += 1
    else:
        for j in range(int(filesystem[i])):
            fileline.append('.')

file = open('output', 'w')

file.write(''.join(fileline))
file.write('\n\n-----------------------------------------------------------------------------------------------------\n\n')

j = len(fileline) - 1
for i in range(len(fileline)):
    if i == j: break

    if(fileline[i] == '.'):
        while(fileline[j] == '.'):
            j -= 1
        fileline[i] = fileline[j]
        fileline[j] = '.'

file.write(''.join(fileline))
file.close()

checksum = 0
for i in range(len(fileline)):
    if fileline[i] == '.': break
    checksum += i*int(fileline[i])
print(checksum) # 100 times lower than right answer