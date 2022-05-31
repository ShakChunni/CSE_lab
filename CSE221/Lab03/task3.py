import sys
from task1 import *
visited = {}
parent = {}
output = []
for node in vertex:
    visited[node] = False
    parent[node] = None
def dfs(start):
    visited[start] = True
    output.append(start)
    for neighbours in Graph.adjency_list[start]:
        if visited[neighbours] == False:
            parent[neighbours] = start
            dfs(neighbours)

sys.stdout = open('output3.txt', 'w')
dfs('1')
for i in range(len(output)):
    if output[i] == '5':
        break
    print(output[i], end=" ")
sys.stdout.close()
