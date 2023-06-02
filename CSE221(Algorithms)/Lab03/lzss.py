file = open("input.txt","r")
rowNumber = file.readline()
graph = {}
for line in file:
    line = line.rstrip()
    x = line.split(" ")
    a = x[0]
    b = x[1:]
    graph[a] = b





visited = [0]*12
queue = []

def BFS(visited, graph, node, endPoint):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        if m == endPoint:
            break
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


#BFS(visited, graph, "1" ,"12")

#print(graph)
visited = [0]*12
printed = []
def DFS_visit(visited, graph, node):
    visited.append(node)
    printed.append(node)
    while queue
