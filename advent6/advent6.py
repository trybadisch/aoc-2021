#!/usr/bin/python3

with open("input6") as f:
    lines = f.readlines() 
fish = lines[0].strip().split(",")

def reset_age():
    age = [0]*9
    for i in range(len(fish)):
        age[int(fish[i])] += 1
    return age

def timeline(days, option):
    age = reset_age()
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
        
        # print distribution
        if option == "y" and i == days:
            print("\nDay ", i, "\t Total: ", count, " - New: ", age[8], sep="")
            for i in range(len(age)):
                print("Age[", i, "]: ", "█" * int((age[i]/count)*250), sep="")
            
    return count

option = input("Show distribution? [Y/N]: ").lower()
part1 = timeline(80, option)
part2 = timeline(256, option)
print("\n[+] Day 6-1:", part1)
print("[+] Day 6-2:", part2)
