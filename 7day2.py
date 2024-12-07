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

def executeOpersArrayWithConcat(opersArray: list[str], numsArray, concatArray: list[str]) -> int:
    result = int(numsArray[0])
    for i in range(1, len(numsArray)):
        if concatArray[i-1] == '1' :
            string = str(result) + str(numsArray[i])
            result = int(string)
        else:
            result = executeOper(result, opersArray[i-1], numsArray[i])
    return result
        

def checkStr(array: list[str]) -> int:
    array[0] = array[0][:len(array[0]) - 1]
    result = int(array[0])
    array = array[1:]
    opersArr = createArray(len(array) - 1, '0')
    for i in range(2**(len(array) - 1)):
        if executeOpersArray(opersArr, array) == result: return result
        concatArray = createArray(len(array) - 1, '0')
        for i in range(2**(len(array) - 1)):
            if executeOpersArrayWithConcat(opersArr, array, concatArray) == result: return result
            perebor( concatArray )
        perebor( opersArr )
    return 0

sum = 0
index = 0
for inputstr in getinput(7).split('\n'):
    print(index)
    if inputstr == '': continue
    sum += checkStr(inputstr.split())
    index += 1
print(sum)
# 11387

# a = 2
# b = 5
# string = str(a) + str(b)
# result = int(string)
# print(result + 1)
