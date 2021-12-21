#!/usr/bin/python3

with open("input17") as f:
    lines = f.readlines()[0].split(": ")[1]

tar_x, tar_y = lines.split(", ")
tar_x = [int(x) for x in tar_x.split("=")[1].split("..")]
tar_y = [int(y) for y in tar_y.split("=")[1].split("..")]

max_y = []
valid = set()

def launch(vx, vy, x=0, y=0, tmp=0):
    global sav_vx, sav_vy  # initial velocity deepcopy
    x += vx; y += vy  # increase position by velocity
    # adjust velocity
    vx += 1 if vx < 0 else (-1 if vx > 0 else 0)
    vy -= 1

    tmp = y if y > tmp else tmp  # save max y

    # check if inside target
    if x >= tar_x[0] and x <= tar_x[1]:
        if y >= tar_y[0] and y <= tar_y[1]:
            max_y.append(tmp)
            valid.add((sav_vx, sav_vy))
            return

    # check if probe hasn't overshoot
    if x <= tar_x[1] and y >= tar_y[0]:
        launch(vx, vy, x, y, tmp)
        return

# hardcoded values to avoid max recursion
for vx in range(0,300):
    for vy in range(-150,150):
        sav_vx = vx; sav_vy = vy
        launch(vx, vy)

print("[+] Max:", max(max_y))
print("[+] Valid:", len(valid))
