import numpy as np


with open("day1.txt") as f:
    data= f.readlines()
    directions = []
    distances = []
    for line in data:
        directions.append(line[0])
        distances.append(int(line[1:]))


def part1():
    pos = 50
    counter=0
    for direction,distance in zip(directions,distances):
        
        if direction == 'R':
            pos+=distance
            if pos >= 100 or pos <= 0:
                pos = pos % 100 
        elif direction == 'L':
            pos-=distance
            if pos >= 100 or pos <= 0:
                pos = pos % 100
        if pos == 0:
            counter+=1
    return counter

def how_may_zeros(dir, dist, start):
    pos = start
    zeros = 0
    if dir == "R":
        for jj in range(dist):
            pos+=1
            if pos == 100:
                pos=0
                zeros+=1
    else:
        for jj in range(dist):
            pos-=1
            if pos == 0:
                zeros+=1
            elif pos==-1:
                pos=99
    return zeros, pos

def part2():
    pos = 50
    counter2 = 0
    for direction,distance in zip(directions,distances):
        count_this_round, pos = how_may_zeros(direction, distance, pos)
        counter2 += count_this_round

    return counter2





print("answer part 1:", part1())
print("answer part 2:", part2())