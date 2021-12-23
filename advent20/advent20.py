#!/usr/bin/python3

with open("input20") as f:
    lines = f.readlines()

algo, image = "".join(lines).split("\n\n")
image = image.split("\n")[:-1]

enhanced = []; new_image = []
switch = 0

def direction():
    d = [ (-1,-1), (-1,0), (-1,+1),
          (0,-1), (0,0), (0,+1),
          (+1,-1), (+1,0), (+1,+1)
    ]
    return d

def enlarge(image):  # enlarge image
    global switch  # change infinity value on each iteration
    char = "." if switch == 0 else "#"
    
    for i in range(2):
        image.insert(0, char*len(image[2]))
        image.append(char*len(image[2]))
    for x in range(len(image)):
        image[x] = (char*2) + image[x] + (char*2)
        
    switch = (switch+1)%2

def enhance(cycles, image=image):
    global enhanced, new_image
    cycles -= 1

    enlarge(image)

    # enhance image
    enhanced = []
    for x in range(len(image)):
        new_line = []
        for y in range(len(image[x])):
            d = direction()
            string = ""
            for i in d:
                try:
                    nx = x+i[0]; ny = y+i[1]
                    if image[nx][ny] == "#":
                        string += "1"
                    else:
                        string += "0"
                except IndexError:
                    string += "0"
            new_line.append(int(string, 2))
        enhanced += [new_line]  # algorithm values
    
    enhanced[-1][-1] = 504 if switch == 0 else 0  # fix last char
    
    # convert enhanced string to image
    new_image = []
    for x in enhanced:
        new_line = []
        for y in x:
            if algo[y] == "#":
                new_line += "#"
            else:
                new_line += "."
        new_image += ["".join(new_line)]
    
    if cycles > 0:
        enhance(cycles, new_image)
    else:
        return

def result(cycles):
    counter = 0
    for x in new_image[int(cycles*1.5):-cycles]:
        for y in x[cycles:-cycles]:
            if y == "#":
                counter += 1
            # print(y, end="")
        # print()
    return counter

cycles = 2
enhance(cycles)
print("[+] Day 20-1:", result(cycles))

cycles = 50
enhance(cycles)
print("[+] Day 20-2:", result(cycles))
