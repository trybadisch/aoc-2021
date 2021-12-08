#!/usr/bin/python3

with open("input2") as f:
    lines = f.readlines()

def part1():
    forward = depth = 0
    for i in lines:
        if "forward" in i:
            forward += int(i[-2:-1])
        elif "up" in i:
            depth -= int(i[-2:-1])
        elif "down" in i:
            depth += int(i[-2:-1])
    return(forward * depth)

def part2():
    forward = depth = aim = 0
    for i in lines:
        if "forward" in i:
            forward += int(i[-2:-1])
            depth += aim * int(i[-2:-1])
        elif "up" in i:
            aim -= int(i[-2:-1])
        elif "down" in i:
            aim += int(i[-2:-1])
    return(forward * depth)

print("[+] Part 1:", part1())
print("[+] Part 2:", part2())
