import sys
from heapq import heappop, heappush
 
class Edge:
    def __init__(self, source, edge, weight):
        self.source = source
        self.edges = edge
        self.weight = weight
 

class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight
 
 
class Graph:
    def __init__(self, edges, nodes):
        self.adjacency_list = [[] for _ in range(nodes)]
        for i in edges:
            self.adjacency_list[i.source].append(i)
 
 
def get_path(previous, var, path):
    if var >= 0:
        get_path(previous, previous[var], path)
        path.append(var)
 
def dijkstra(graph, source, total_vertices, destination):
    min_heap = []
    heappush(min_heap, Node(source, 0))
    distance = [sys.maxsize] * total_vertices
    distance[source] = 0
    visited = [False] * total_vertices
    visited[source] = True
    previous = [-1] * total_vertices
    path = []
    while min_heap:
        u = heappop(min_heap)      
        current_vertex = u.vertex         
        for i in graph.adjacency_list[current_vertex]:
            v = i.edges
            weight = i.weight
            if not visited[v] and (distance[current_vertex] + weight) < distance[v]:
                distance[v] = distance[current_vertex] + weight
                previous[v] = current_vertex
                heappush(min_heap, Node(v, distance[v]))
        visited[current_vertex] = True

    if total_vertices == 2:
        print(1)
 
    for i in range(1, total_vertices):
        if i != source and distance[i] != sys.maxsize:
            get_path(previous, i, path)
            if i == destination:
                for i in range(0, len(path)):
                    print(path[i], end=" ")
            path.clear()

 
 
input_file = open('input2.txt', 'r')
input_file = input_file.read()
sys.stdout = open('output2.txt', 'w')
input_array = input_file.split('\n')

#spliting

test_case = input_array[0].split()
l2 = input_array[1].split() 
l3 = input_array[2].split() #l
l4 = input_array[3].split()
l5 = input_array[4].split() #l
l6 = input_array[5].split()
l7 = input_array[6].split()
l8 = input_array[7].split()
l9 = input_array[8].split()
l10 = input_array[9].split()
l11 = input_array[10].split()

for i in range(len(l2)):
    l2[i] = int(l2[i])
for i in range(len(l4)):
    l4[i] = int(l4[i])
for i in range(len(l6)):
    l6[i] = int(l6[i])
for i in range(len(l7)):
    l7[i] = int(l7[i])
for i in range(len(l8)):
    l8[i] = int(l8[i])
for i in range(len(l9)):
    l9[i] = int(l9[i])
for i in range(len(l10)):
    l10[i] = int(l10[i])
for i in range(len(l11)):
    l11[i] = int(l11[i])


edges2 = [Edge(l4[0], l4[1], l4[2])]
edges1 = [Edge(l2[0], l2[1], 0)]
edges3 = [Edge(l6[0], l6[1], l6[2]), Edge(l7[0], l7[1], l7[2]), Edge(l8[0], l8[1], l8[2]), Edge(l9[0], l9[1], l9[2]), Edge(l10[0], l10[1], l10[2]), Edge(l11[0], l11[1], l11[2])]
first_case = 2
second_case = 3
third_case = 6
graph1 = Graph(edges1, first_case)
graph2 = Graph(edges2, second_case)
graph3 = Graph(edges3, third_case)
source1 = l2[0] 
source2 = l4[0]
source3 = l7[0]
dijkstra(graph1, source1, first_case, l2[1])
dijkstra(graph2, source2, second_case, l4[1])
print(" ")
dijkstra(graph3, source3, third_case, l6[1])



sys.stdout.close()

