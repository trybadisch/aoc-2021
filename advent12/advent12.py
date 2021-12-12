#!/usr/bin/python3

with open("input12") as f:
    lines = f.readlines()

graph = {}  # adjacency list -> { a: [b,c], b: [a,c] }
for l in lines:
    x,y = l.strip().split("-")
    graph[x] = [y] if x not in graph else graph[x] + [y]
    graph[y] = [x] if y not in graph else graph[y] + [x]

# call recursively with a copy of visited paths to branch itself
def search(node, visited, part, twice=False):
    global paths
    visited += [node]
    if node == "end":  # add path and return
        if visited not in paths:
            paths += [visited]
        return
    
    for neighbour in graph[node]:  # check adjacent nodes
        if neighbour.isupper() or neighbour not in visited:
            search(neighbour, visited.copy(), part, twice)
            
        if part==2:  # visit lowercase twice if flag isn't set yet
            if neighbour.islower() and not twice and neighbour != "start":
                search(neighbour, visited.copy(), part, True)

paths = []
search("start", [], 1)
print("[+] Part 1 Result: ", len(paths))
print("Calculating Part 2... [~3 min]")
paths = []
search("start", [], 2)
print("[+] Part 2 Result : ", len(paths))
