# me
from getinput import getinput

def safeNoDamper(report) -> bool:
    ascFlag = int(report[0]) - int(report[1]) < 0
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i+1])
        if(not(1 <= abs(diff) <= 3) or (diff < 0) != ascFlag):
            return False
    return True

def safe(report) -> bool:
    ascFlag = int(report[0]) - int(report[1]) < 0
    # 1 10 9 8 7 6
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i+1])
        if(not(1 <= abs(diff) <= 3) or (diff < 0) != ascFlag):
            return safeNoDamper(report[:i+1] + report[i+2:]) or safeNoDamper(report[:i] + report[i+1:])
    return True

sum = 0
for report in getinput(2).split('\n'):
    if(len(report) > 0 and safe(report.split(' '))):
        sum += 1
print(sum)



# @Ioann44 
from typing import Iterable

def get_substracted(report: list[int]) -> Iterable[list[int]]:
    for i in range(len(report)):
        yield report[:i] + report[i+1:]

def check(report: list[int], is_ascending: bool) -> bool:
    res = [1,2,3] if is_ascending else [-1,-2,-3]
    for rep in get_substracted(report):
        diffs = {rep[i+1] - rep[i] for i in range(len(rep) - 1)}
        if len(diffs.difference(res)) == 0:
            return True
    return False

print(sum(1 for report in getinput(2).split('\n') if report and (int_rep := [int(num) for num in report.split(' ')]) and (check(int_rep, False) or check(int_rep, True))))
