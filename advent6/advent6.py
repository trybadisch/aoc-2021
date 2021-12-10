#!/usr/bin/python3

with open("input6") as f:
    lines = f.readlines() 
fish = lines[0].strip().split(",")

def reset_age():
    age = [0]*9
    for i in range(len(fish)):
        age[int(fish[i])] += 1
    return age

def timeline(days):
    age = reset_age()
    print("\nStart state:", age, "\n")
    for i in range(1,days+1):
        aux = age[0]
        for j in range(len(age)):
            if j != 8:
                age[j] = age[j+1]
        age[6] += aux
        age[8] = aux
        
        count = 0
        for k in range(len(age)):
            count += age[k]
            
        if i == days:
            print("Day ", i, "\t Total: ", count, " - New: ", age[8], sep="")
            # print final distribution
            for i in range(len(age)):
                print("Age[", i, "]: ", "█" * int((age[i]/count)*250), sep="")
            print()
            
    print("Final state: ", age, "\n", "-" * 50, sep="")
    return count
    
part1 = timeline(80)
part2 = timeline(256)
print("\n[+] Day 80 =", part1)
print("[+] Day 256 =", part2, "\n")
