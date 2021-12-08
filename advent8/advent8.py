#!/usr/bin/python3

with open("input8") as f:
    lines = f.readlines()

digits1 = list(i.split("|")[0].strip() for i in lines)
digits2 = list(i.split("|")[1].strip() for i in lines)

known = {2:1,3:7,4:4,7:8}  # 1, 4, 7, 8

''' 
Repetitions     In known            Rule

a = 8           7, 8            only in 7,8 (not in 1,4)
b = 6           4, 8            6 times
c = 8           1,4,7,8         8 times AND not A
d = 7           4, 8            7 times AND not G
e = 4           8               4 times
f = 9           1,4,7,8         9 times
g = 7           8               7 times AND only in 8 (not in 1,4,7)
'''

def part1():
    count = 0
    for i in digits2:
        dig = i.split(" ")
        for j in dig:
            if len(j) in known:
                count += 1
    return (count)

def part2():
    total_count = 0
    for i in range(len(digits1)):
        nums = {1:"",4:"",7:"",8:""}    # known number strings
        reps = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0}          # char repetitions
        normal = {"a":"","b":"","c":"","d":"","e":"","f":"","g":""} # map to standard
        display = {"abcefg":0,"cf":1,"acdeg":2,"acdfg":3,"bcdf":4,
        "abdfg":5,"abdefg":6,"acf":7,"abcdefg":8,"abcdfg":9}        # standard display chars
        
        # get char repetitions
        for j in range(len(digits1[i])):
            if digits1[i][j] in reps:
                reps[digits1[i][j]] += 1
        
        # get known digits
        dig1 = digits1[i].split(" ")
        dig1 = ["".join(sorted(x)) for x in dig1]
        for j in dig1:
            if len(j) in known:
                nums[known[len(j)]] = j
        
        # map chars into position
        for ch in reps:
            if reps[ch] == 4:
                normal["e"] = ch
            elif reps[ch] == 6:
                normal["b"] = ch
            elif reps[ch] == 9:
                normal["f"] = ch
            elif reps[ch] == 7:
                if ch in nums[8] and ch not in (nums[1]+nums[4]+nums[7]):
                    normal["g"] = ch
                else:
                    normal["d"] = ch
            elif reps[ch] == 8:
                if ch in (nums[7]+nums[8]) and ch not in (nums[1]+nums[4]):
                    normal["a"] = ch
                else:
                    normal["c"] = ch
        
        # substitution & search in display
        display_count = []
        dig2 = digits2[i].split(" ")
        dig2 = ["".join(sorted(x)) for x in dig2]
        for j in dig2:
            new = [list(normal.keys())[list(normal.values()).index(k)] for k in j]
            sort = "".join([x for x in sorted(new)])
            if sort in display:
                display_count.append(str(display[sort]))

        print("[", *dig1, "|", *dig2, "]")
        display_count = int("".join(display_count))
        print("[ Display: ", display_count, "]\n")
        total_count += display_count
        
    return total_count

part1 = part1()
part2 = part2()
print("[+] Part 1 Result: ", part1)
print("[+] Part 2 Result: ", part2, "\n")
