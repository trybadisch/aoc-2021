#!usr/bin/python3

with open("input3") as f:
    lines = f.readlines()

matrix = []

def reset_matrix():
    for i in range(12):
        matrix.append(0)

def part1():
    reset_matrix()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            value = lines[i][j]
            if value == "1":
                matrix[j] += 1
            
    gamma = ""
    for i in range(len(matrix)):
        gamma += "1" if matrix[i] > (len(lines))/2 else "0"

    gamma = int(gamma, 2)
    epsilon = ~gamma & 0xFFF

    print(matrix, "\n", bin(gamma), "\n", bin(epsilon), sep="")
    print("\n[+] Part 1 Result:", gamma * epsilon)
    print("-" * 25, "\n")

part1()

'''---------- Part 2 ----------'''
def key_sum(key):
    total = 0
    for i in range(len(lines)):
        if key == 0 or lines[i][0:key] == gamma[0:key]:
            total += 1
            value = lines[i][key]
            if value == "1":
                matrix[key] += 1
    print("Total: ", total, "\tMx[",key,"]: ", matrix[key], end="\t", sep="")
    if key != 0:
        print("Chain:", gamma[0:key])
    else:
        print()
    return total
    
def print_matrix(gamma, bit):
    print("-" * 25)
    print("Matrix ", bit, "s: ", matrix, sep="")
    print(bit, "s Result: ", gamma, " ( ", bin(gamma), " ) ", sep="")
    print("-" * 25)

# get 1s matrix
gamma = ""
matrix = []
reset_matrix()
for i in range(12):
    total = key_sum(i)
    gamma += "1" if matrix[i] >= total/2 else "0"
gamma1 = int(gamma, 2)
print_matrix(gamma1, 1)

# get 0s matrix
gamma = ""
matrix = []
reset_matrix()
for i in range(12):
    total = key_sum(i)
    gamma += "1" if matrix[i] < total/2 else "0"
gamma0 = int(gamma, 2)
print_matrix(gamma0, 0)

print("\n[+] Part 2 Result:", gamma1 * gamma0, "\tCHECK IF BINARY VALUES EXIST\n")
