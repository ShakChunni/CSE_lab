# I modfied the input.txt file, Because it caused error as tabs were used to separate the numbers. 
# I modified the input from tabs to spaces.
# M[45]Sifat Tanvir sir said it was okay. 


class Graph:
    adjency_list = {}
    def __init__(self, vertex):
        self.vertex = vertex       
        for i in self.vertex:
            Graph.adjency_list[i] = [] 
    
    def add_edge(self, vertex, edge):
        Graph.adjency_list[vertex].append(edge)
       

input_file = open('input.txt', 'r')
input_file = input_file.read()
#sys.stdout = open('output1.txt', 'w')
input_array = input_file.split('\n')

#spliting

input_array_line1 = input_array[0].split()
l2 = input_array[1].split()
l3 = input_array[2].split()
l4 = input_array[3].split()
l5 = input_array[4].split()
l6 = input_array[5].split()
l7 = input_array[6].split()
l8 = input_array[7].split()
l9 = input_array[8].split()
l10 = input_array[9].split()
l11 = input_array[10].split()
l12 = input_array[11].split()  
l13 = input_array[12].split()  

vertex = [l2[0], l3[0], l4[0], l5[0], l6[0], l7[0], l8[0], l9[0], l10[0], l11[0], l12[0], l13[0]]
edges = [(l2[0], l2[1]), (l3[0], l3[1]), (l3[0], l3[2]), (l3[0], l3[3]), (l4[0], l4[1]), (l4[0], l4[2]), (l4[0], l4[3]), (l6[0], l6[1]), (l6[0], l6[2]), 
(l7[0], l7[1]), (l7[0], l7[2]), (l8[0], l8[1]), (l9[0], l9[1]), (l9[0], l9[2]), (l10[0], l10[1]), (l11[0], l11[1]), (l12[0], l12[1])]
graph = Graph(vertex)
for v, e in edges:
    graph.add_edge(v, e)
#graph.print_graph()
#graph.bfs(l2[0], l13[0])

#graph.bfs()
#graph.dfs()

