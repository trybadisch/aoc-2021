#!/usr/bin/python3

with open("input1") as f:
    lines = f.readlines()

def triple_sum(key):  # sum range(3)
    total = 0
    if (key+2) < len(lines):
        for i in range(3):
            total += int(lines[i+key])
    return total

def part(part):
    count = prev = 0
    for key in range(len(lines)):
        # sum from part context
        num = int(lines[key]) if part==1 else triple_sum(key)
        if num > prev and prev != 0:
            count += 1
        prev = num
    return count

print("[+] Part 1:", part(1))
print("[+] Part 2:", part(2))
