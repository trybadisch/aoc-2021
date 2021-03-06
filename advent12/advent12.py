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
    visited.append(node)
    if node == "end":  # add path and return
        paths.add(tuple(visited))
        return
    
    for neighbour in graph[node]:  # check adjacent nodes
        if neighbour.isupper() or neighbour not in visited:
            search(neighbour, visited.copy(), part, twice)
            
        if part==2:  # visit lowercase twice if flag isn't set yet
            if neighbour.islower() and not twice and neighbour != "start":
                search(neighbour, visited.copy(), part, True)

paths = set()
search("start", [], 1)
print("[+] Day 12-1:", len(paths))
search("start", [], 2)
print("[+] Day 12-2:", len(paths))
