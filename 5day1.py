from getinput import getinput
# from typing import Dict


# def middleIfCorrect(array: list[str], dict: Dict[str, list[str]]) -> int:
#     for i in range(1, len(array)):
#         for j in range(i):
#             if(array[i] in dict and array[j] in array[i]):
#                 return 0
#     return int(array[len(array)//2])


# dict: Dict[str, list[str]] = {}
# rulesover = False
# sum = 0
# for item in getinput(0).split('\n'):
#     if(item.strip() == ''): 
#         rulesover = True

#     if(rulesover):
#         if(item.strip() == ''): continue
#         sum += middleIfCorrect(item.split(','), dict)
#     else:
#         numbers = item.split('|')
#         if(numbers[0] in dict):
#             dict[numbers[0]].append(numbers[1])
#         else:
#             dict[numbers[0]] = [numbers[1]]
        
# print(sum) i suck

        