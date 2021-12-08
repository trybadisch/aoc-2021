#!/usr/bin/python3

from PIL import Image

with open("input5") as f:
    lines = f.readlines()

matrix = []

def new_matrix():
    size = 1000
    for x in range(size):
        tmp_mx = []
        for y in range(size):
            tmp_mx.append(0)
        matrix.append(tmp_mx)

def aligned(x1,y1,x2,y2):  # call from mark_matrix()
    # invert values to get positive progession
    if x1 > x2:
        tmp = x1; x1 = x2; x2 = tmp
    if y1 > y2:
        tmp = y1; y1 = y2; y2 = tmp
    
    if x1 == x2:  # horizontal line
        for y in range(y1, y2+1):
            matrix[x1][y] += 1
    elif y1 == y2:  # vertical line
        for x in range(x1, x2+1):
            matrix[x][y1] += 1

def diagonal(x1,y1,x2,y2):  # call from mark_matrix()
    aux = 0  # value "loops" y axis
    
    def vertical_dir(x,y1,y2,aux):  # inner function checks for y axis
        if y1+aux <= y2:  # positive y
            matrix[x][y1+aux] += 1
        elif y1-aux >= y2:  # negative y
            matrix[x][y1-aux] += 1
        return (aux+1)  # increase aux every loop
    
    if x1 < x2:  # positive x
        for x in range(x1, x2+1):
            aux = vertical_dir(x,y1,y2,aux)
    elif x1 > x2:  # negative x
        for x in range(x1, x2-1, -1):
            aux = vertical_dir(x,y1,y2,aux)

def mark_matrix():
    part2 = input("Check diagonals (Part 2)? [Y/N]: ").lower()
    for i in lines:
        aux1, aux2 = i.split("-> ")
        y1, x1 = aux1.split(",")
        y2, x2 = aux2.split(",")
        
        x1 = int(x1); x2 = int(x2); y1 = int(y1); y2 = int(y2)  # convert to int

        if x1==x2 or y1==y2:  # horizontal & vertical
            aligned(x1,y1,x2,y2)
        else:  # diagonals
            if part2 == "y":
                diagonal(x1,y1,x2,y2)

def check():
    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] > 1:
                count += 1
    print("\n[+] Overlaps:", count,"\n")

def output():
    option = input("Show ASCII matrix? [Y/N]: ").lower()
    if option == "y":
        output = "\n"
        for x in matrix:
            for y in x:
                output += "." if y == 0 else str(y)
            output += "\n"
        print(output)
        
def save_image():  # pillow module
    option = input("Save image? [Y/N]: ").lower()
    if option == "y":
    
        def get_colors(x,y):  # inner function gets color for coordinates
            colors = (
                (matrix[x][y] ** 6) % 255,
                (matrix[x][y] * 50) % 255,
                (matrix[x][y] * 25) % 255
            )
            return colors
    
        img = Image.new("RGB", [len(matrix),len(matrix)], 255)
        data = img.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                data[x,y] = get_colors(x,y)  # get colors
                
        # heatmap surrounding pixels
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if matrix[x][y] >= 2:
                    for i in range(-1,2):
                        data[x+i,y+i] = data[x+i,y-i] = data[x+i,y] = data[x,y+i] = get_colors(x,y)  # get colors
        img.save("image.png")
        print("Image saved as image.png")

new_matrix()
mark_matrix()
check()
output()
save_image()
