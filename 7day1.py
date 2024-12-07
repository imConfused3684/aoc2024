from getinput import getinput
import operator

arr = [1, 2, 3, 4]
# * * *
# * * +
# * + *
# * + +
# + * *
# + * +
# + + *
# + + +

# 3 = 2**3

def perebor(variant: list[str]) -> list[str]:
    one_in_mind = False
    if variant[-1] == '1': one_in_mind = True; variant[-1] = '0'
    else: variant[-1] = '1'; return variant
    
    for i in reversed(range(len(variant) - 1)):
        if one_in_mind:
            if variant[i] == '1': variant[i] = '0'
            elif variant[i] == '0': one_in_mind = False; variant[i] = '1'
        else:
            return variant

def createArray(length: int, symbol: str) -> list[str]:
    array = []
    for i in range(length):
        array.append(symbol)
    return array

opers = { '0' : operator.add, '1' : operator.mul }
def executeOper(op1, oper: str, op2):
    op1, op2 = int(op1), int(op2)
    return opers[oper](op1, op2)

def executeOpersArray(opersArray: list[str], numsArray) -> int:
    result = int(numsArray[0])
    for i in range(1, len(numsArray)):
        result = executeOper(result, opersArray[i-1], numsArray[i])
    return result
        

def checkStr(array: list[str]) -> int:
    array[0] = array[0][:len(array[0]) - 1]
    result = int(array[0])
    array = array[1:]
    opersArr = createArray(len(array) - 1, '0')
    for i in range(2**(len(array) - 1)):
        if executeOpersArray(opersArr, array) == result: return result
        perebor( opersArr )
    return 0

sum = 0
for str in getinput(7).split('\n'):
    if str == '': continue
    sum += checkStr(str.split())
print(sum)


# str = '134542353423:'
# str = str[:len(str)-1]
# print(str)

# str = 'penis'
# print(str[1:])

# print(executeOpersArray(['0','0','1'], [8,9,2,3]))


# length = 4
# lengthOper = length - 1
# opersArr = createArray(lengthOper, '0')
# for i in range(2**lengthOper):
#     print( opersArr )
#     perebor(opersArr)