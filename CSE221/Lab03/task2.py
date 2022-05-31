import sys
from queue import Queue
from task1 import *
def bfs(start, destination):
    visited = {}
    parent = {}
    output = []
    queue = Queue()
    for node in vertex:
        visited[node] = False
        parent[node] = None
    source = start
    visited[source] = True
    queue.put(source)
    while not queue.empty():
        m = queue.get()
        output.append(m)
        if m == destination:
            break
        for neighbour in Graph.adjency_list[m]:
            if not visited[neighbour]:
                visited[neighbour] = True
                parent[neighbour] = m
                queue.put(neighbour)
    for i in range(len(output)):
        print(output[i], end=" ")

sys.stdout = open('output2.txt', 'w')
bfs('1', '12')
sys.stdout.close()
