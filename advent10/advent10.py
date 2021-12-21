#!/usr/bin/python3

with open("input10") as f:
    lines = [l.strip() for l in f.readlines()]

op = { "(":")", "[":"]", "{":"}", "<":">" }
ed = { ")":"(", "]":"[", "}":"{", ">":"<" }
points = { ")":(3,1), "]":(57,2), "}":(1197,3), ">":(25137,4) }

p1 = 0
p2 = []

for l in lines:
    queue = []
    corrupt = False
    for c in l:
        if c in op:
            queue.append(c)  # add open brackets to queue
        else:
            if queue[-1] == ed[c]:
                queue.pop()  # remove bracket if closed
            else:
                corrupt = True
                p1 += points[c][0]
                break
    
    if not corrupt:  # part 2
        complete = []
        score = 0
        # reverse queue and translate into closed bracket
        for c in reversed(queue):
            complete.append(op[c])
            score = (score*5) + points[complete[-1]][1]
        p2.append(score)
     
print("[+] Day 10-1:", p1)
result = sorted(p2)[len(p2)//2]
print("[+] Day 10-2:", result)
