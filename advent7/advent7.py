#!/usr/bin/python3

with open("input7") as f:
    crabs = [int(i) for i in f.readlines()[0].strip().split(",")]

median = sorted(crabs)[len(crabs)//2]
fuel = sum([abs(median-i) for i in crabs])
print("[+] Part 1: Median =", median, "/ Fuel =", fuel)

mean = sum(crabs)//len(crabs)
fuel = sum([abs(mean-i) * (abs(mean-i)+1) // 2 for i in crabs])
print("[+] Part 2: Mean =", mean, "/ Fuel =", fuel)

''' Bruteforce Part 2:
fuel = pos = 0
for i in range(max(crabs)):
    tmp = 0
    for j in crabs:
        dif = abs(i - j)
        tmp += dif * (dif+1) // 2
    if tmp < fuel or fuel == 0:
        fuel = tmp
        pos = i
print("[+] Position =", pos, "/ Fuel =", fuel)
'''
