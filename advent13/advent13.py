#!/usr/bin/python3

''' Parsing block '''
with open("input13") as f:
    lines = f.readlines()

coords, folds = "".join(lines).strip().split("\n\n")
coords = coords.split("\n")
folds = folds.split("\n")

mat = [0]*len(coords)
fold = []

for c in range(len(coords)):
    x,y = coords[c].split(",")
    mat[c] = (int(x), int(y))

for f in range(len(folds)):
    left,right = folds[f].split("=")
    if left[-1] == "x":
        fold += [("x", int(right))]
    elif left[-1] == "y":
        fold += [("y", int(right))]

# get max sheet coordinates
for i in range(len(fold[:2])):
    if fold[i][0] == "x":
        mx = fold[i][1]*2
    elif fold[i][0] == "y":
        my = fold[i][1]*2

sheet = []
for i in range(my+1):
    sheet += [[" "] * (mx+1)]

for i in range(len(mat)):
    x,y = mat[i][0], mat[i][1]
    sheet[y][x] = "█"

''' Folding logic:
    Invert & add other half values: [0] += [-1], [1] += [-2], etc '''

def fold_ver(half):
    global sheet
    c = 0
    for i in range(len(sheet)-1, half, -1):
        for j in range(len(sheet[i])):
            if sheet[i][j] == "█":
                sheet[c][j] = "█"
        c += 1
    sheet = sheet[:half]

def fold_hor(half):
    global sheet
    for i in range(len(sheet)):
        c = 0
        for j in range(len(sheet[i])-1, half, -1):
            if sheet[i][j] == "█":
                sheet[i][c] = "█"
            c += 1
    for y in range(len(sheet)):
        sheet[y] = sheet[y][:half]

def print_sheet():
    string = ""
    for i in range(len(sheet)):
        for j in sheet[i]:
            string += j
        string += "\n"
    return string

# check fold instructions
def check_folds():
    for i in range(len(fold)):
        half = fold[i]
        if half[0] == "y":
            fold_ver(half[1])
        elif half[0] == "x":
            fold_hor(half[1])
            
        if i == 0:  # Part 1: first fold
            first = 0
            for i in range(len(sheet)):
                for j in range(len(sheet[i])):
                    first = first+1 if sheet[i][j] == "█" else first
    return first

print("[+] Part 1 Result:", check_folds())
print("[+] Part 2 Result:\n\n", print_sheet(), sep="")
