#!/usr/bin/python3

with open("input14") as f:
    lines = f.readlines()

poly, rules = "".join(lines).strip().split("\n\n")

alpha = {}; pairs = {}; eq = {}
for i in rules.split("\n"):
    pair, char = i.split(" -> ")
    alpha[char] = 0
    pairs[pair] = 0
    eq[pair] = char

# starting values
for i in range(len(poly)-1):
    a = poly[i]; b = poly[i+1]
    alpha[a] += 1
    pairs[a+b] += 1
alpha[poly[-1]] += 1

''' For every pair, sum the value of its insertion to alpha
    Add the combination of pairs with its insertion and remove the original
    eg: CH: B -> add(CB, BH); remove(CH) '''
def polymer():
    # create deepcopy of pairs count for current iteration
    copy = {}
    for i in pairs:
        copy[i] = pairs[i]
        
    for i in copy:
        alpha[eq[i]] += copy[i]
        pairs[i[0] + eq[i]] += copy[i]
        pairs[eq[i] + i[1]] += copy[i]
        pairs[i] -= copy[i]

def minmax():
    min_a = max_a = 0
    for i in alpha:
        min_a = alpha[i] if alpha[i] < min_a or min_a == 0 else min_a
        max_a = alpha[i] if alpha[i] > max_a or max_a == 0 else max_a
    return(max_a - min_a)

for i in range(10):
    polymer()
print("[+] Day 14-1:", minmax())

for i in range(40-10):
    polymer()
print("[+] Day 14-2:", minmax())
