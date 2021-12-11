#!/usr/bin/python3

import curses
from time import sleep

with open("input11") as f:
    lines = f.readlines()

mat = [[int(y) for y in lines[x] if y.isnumeric()] for x in range(len(lines))]

flashes = sync = cycle = 0

def visualization(screen, speed):
    global cycle, flashes
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    screen.clear()
    
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            if mat[x][y] == 0:
                screen.attron(curses.A_BOLD)
                screen.addstr(str(mat[x][y])+" ")
                screen.attroff(curses.A_BOLD)
            else:
                screen.addstr(str(mat[x][y])+" ")
        screen.addstr("\n")
    screen.addstr("\n[+] Cycle: " + str(cycle))
    screen.addstr("\n[+] Flashes: " + str(flashes))
    screen.refresh()
    sleep(speed)

def direction(x,y):
    d = {
        "up"    : (-1,0) if x > 0 else (0,0),
        "down"  : (+1,0) if x < len(mat)-1 else (0,0),
        "left"  : (0,-1) if y > 0 else (0,0),
        "right" : (0,+1) if y < len(mat[0])-1 else (0,0),
        "uleft" : (-1,-1) if x > 0 and y > 0 else (0,0),
        "uright": (-1,+1) if x > 0 and y < len(mat[0])-1 else (0,0),
        "dleft" : (+1,-1) if x < len(mat)-1 and y > 0 else (0,0),
        "dright": (+1,+1) if x < len(mat)-1 and y < len(mat[0])-1 else (0,0)
    }
    return d

def flash(x,y):
    global flashes, sync
    if mat[x][y] >= 10:
        mat[x][y] = 0
        flashes += 1; sync += 1
        d = direction(x,y)
        for i in d:
            if d[i] != (0,0):
                xn = x + d[i][0]; yn = y + d[i][1]
                if mat[xn][yn] != 0:
                    mat[xn][yn] += 1
                if mat[xn][yn] > 9:
                    flash(xn,yn)

option = input("Show visualization? [Y/N]: ").lower()
if option == "y":
    speed = int(input("Frame speed [0 = Fastest] - [9 = Slowest]: "))
    speed = float("0."+str(speed)) if speed != 0 else 0.05

while True:
    cycle += 1; sync = 0
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            mat[x][y] += 1
    for x in range(len(mat)):
        for y in range(len(mat[x])):
            flash(x,y)
    
    if option == "y":
        curses.wrapper(visualization, speed)
            
    if cycle == 100:
        print("[+] Flashes:", flashes)
    if sync == len(mat)*len(mat[0]):
        print("[+] Synchronization:", cycle, "cycles")
        break
