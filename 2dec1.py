from getinput import getinput

def safe(report) -> bool:
    ascFlag = int(report[0]) - int(report[1]) < 0
    for i in range(len(report) - 1):
        diff = int(report[i]) - int(report[i+1])
        if(not(1 <= abs(diff) <= 3) or (diff < 0) != ascFlag):
            return False
    return True

sum = 0
for report in getinput(0).split('\n'):
    if(len(report) > 0 and safe(report.split(' '))):
        sum += 1
print(sum)