import requests

def getinput(day) -> str:
    if day:
        return requests.get(f'https://adventofcode.com/2024/day/{day}/input', cookies={'session': open('session', 'r').read()}).text
    else:
        return open('test', 'r').read()