#!/usr/bin/python3

with open("input9") as f:
    lines = f.readlines()

# create matrix
mat = [[int(y) for y in lines[x] if y.isnumeric()] for x in range(len(lines))]

global size
height = 0
lows = []; visited = []; basins = []

def check(x,y,part):
    global size
    height = 0
    
    c = mat[x][y]   # current position
    d = {           # direction (x,y) modifier
        "up"    : (-1,0) if x > 0 else (0,0),
        "down"  : (+1,0) if x < len(mat)-1 else (0,0),
        "left"  : (0,-1) if y > 0 else (0,0),
        "right" : (0,+1) if y < len(mat[0])-1 else (0,0)
    }
    
    if part == 1:  # check directions
        if all(c <= mat[x + d[i][0]][y + d[i][1]] for i in d):
            height += c+1
            lows.append((x,y))
            visited.append((x,y))
        return height
    
    elif part == 2:  # check recursively if not visited
        for i in d:
            xn = x + d[i][0]; yn = y + d[i][1]
            if (xn,yn) not in visited and mat[xn][yn] != 9:
                size += 1
                visited.append((xn,yn))
                check(xn,yn,2)
           
for x in range(len(mat)):
    for y in range(len(mat[x])):
        height += check(x,y,1)
print("[+] Part 1 Result:", height)

for i in range(len(lows)):
    size = 1
    check(lows[i][0],lows[i][1],2)
    basins.append(size)
    
# get max 3 values
result = (lambda z : z[0]*z[1]*z[2])([i for i in sorted(basins)[-3:]])
print("[+] Part 2 Result:", result)
