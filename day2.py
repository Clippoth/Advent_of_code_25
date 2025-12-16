import math

with open("day2.txt") as f:
    data = f.read()
    IDs = [[int(first), int(last)] for ID in data.split(',') for first, last in [ID.split('-')]]

def isInvalid(code):
    ID_sum = 0
    if code[0]=='0':
        pass
    else:
        if code[0:int(len(code)/2)]==code[int(len(code)/2):]:
            ID_sum+=int(code)
    return ID_sum

def part1():
    sum = 0
    for IDcouple in IDs:
        for ID in range(IDcouple[0], IDcouple[1]+1):
            if len(str(ID))>1:
                sum+=isInvalid(str(ID))
    return sum

def isInvalid2(code):
    n = len(code)
    # Try all possible block sizes k
    for k in range(1, n):
        if n % k == 0:  
            block = code[:k]
            # Create a fake string that would be the same if the code is 
            # actually made of repetitions of k length 
            if block * (n // k) == code: 
                return int(code)
    return 0


def part2():
    sum = 0
    for IDcouple in IDs:
        for ID in range(IDcouple[0], IDcouple[1]+1):
            if len(str(ID))>1:
                sum+=isInvalid2(str(ID))
    return sum


print("answer part 1:", part1())
print("answer part 2:", part2())