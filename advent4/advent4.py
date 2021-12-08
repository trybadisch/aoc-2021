#!/usr/bin/python3

'''Code to create Bingo 3D matrix'''
with open("input4") as f:
    lines = f.readlines()
    
bingo = lines[0].split(",")  # bingo number list
boards = []  # 3D board matrix

# remove first char of line if space
for i in range(len(lines)):
    if lines[i][0] == " ":
        lines[i] = lines[i][1:]

def board_matrix(key):
    mat1 = []; mat2 = []  # mat1: rows / mat2: cols
    tmp = ""  # readchar until space
    for i in range(5):  # loop 5 lines (board)
        for j in lines[key+i]:
            if not j.isspace():
                tmp += j
            elif len(tmp) != 0:
                mat1.append(tmp)
                tmp = ""
        mat2.append(mat1)
        mat1 = []
    boards.append(mat2)  # append to board list -> [board[col[row]]]
        
for i in range(2, len(lines), 6):  # step through boards' first index
    board_matrix(i)

'''Game code to check winning & losing plays'''
win = []  # bingo numbers already called
win_msg = lose_msg = ""

def finish(key):
    global win_msg, lose_msg
    msg = ""
    sum_count = 0
    for i in boards[key]:
        for j in i:
            msg += j + "\t"
            if j != "X":  # sum remaining values (not X)
                sum_count += int(j)
        msg += "\n\n"
    msg += ( "[+] Sum * Last = " + str(sum_count) + " * " + win[-1] + " = " +
             str(sum_count * int(win[-1])) + "\n" )
    if len(win_msg) == 0:
        win_msg = msg  # win if first bingo
    else:
        lose_msg = msg  # lose if after first (replace until last)
        
    boards.pop(key)  # remove board from list
    
    try:  # repeat until failure
        start()
    except:  # result returned as exception
        exit( "\n[+] Part 1 - Winner board:\n\n" + win_msg + "-"*35 +
            "\n\n[+] Part 2 - Loser board:\n\n" + lose_msg )

def mark_check(key):
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if boards[i][j][k] == key:
                    boards[i][j][k] = "X"
            
            if i > 5:  # check if bingo in the same loop
                if boards[i][j] == ["X","X","X","X","X"]:  # check horizontals
                    finish(i)
                if [boards[i][x][j] for x in range(5)] == ["X","X","X","X","X"]:  # check verticals
                    finish(i)

def start():
    for i in range(len(bingo)):
        if bingo[i] not in win:
            win.append(bingo[i])  # track last called number
        mark_check(bingo[i])  # change value to "X" & check condition

start()
