f = open("input file.txt", "r")
f = f.read()
f = f.split('\n')
main_city = []
city_name = []
straightline_distance = []
neighbour_distance = []
for i in range(len(f)):
    x = f[i].split()
    for j in range(len(x)):
        if j == 0:
            main_city.append(x[0])
        elif j == 1:
            straightline_distance.append(x[j])
        elif j % 2 == 0:
            city_name.append(x[j])
        elif j % 2 != 0:
            neighbour_distance.append(x[j])


nei_distance = [eval(i) for i in neighbour_distance]  # int te conversion
straightline_distance = [eval(i) for i in straightline_distance]

listx = []
for i in range(len(nei_distance)):
    listx.append([city_name[i], nei_distance[i]])

len_x = []
for i in range(len(f)):  # total no of input input index per line
    x = f[i].split()
    len_x.append(len(x))

# print(len_x) #[8 3, 8, 4 1, 6 2, 4, 6, 4, 10, 6, 8, 8, 6, 6, 6, 6, 6, 8, 6, 6, 10]
abc = []
# condtions to check length of each line after strgt_dis and main_city shoraisi (idk me stupid)
for i in range(0, len(len_x)):
    if i == 0:
        if len_x[i] == 2:
            cond = listx[0:0]
            new_start = 0
        if len_x[i] == 4:
            cond = listx[0:1]
            new_start = 1
        elif len_x[i] == 6:
            cond = listx[0:2]
            new_start = 2
        elif len_x[i] == 8:
            cond = listx[0:3]
            new_start = 3
        elif len_x[i] == 10:
            cond = listx[0:4]
            new_start = 4
        elif len_x[i] == 12:
            cond = listx[0:5]
            new_start = 5
        elif len_x[i] == 14:
            cond = listx[0:6]
            new_start = 6
        elif len_x[i] == 16:
            cond = listx[0:7]
            new_start = 7
        elif len_x[i] == 18:
            cond = listx[0:8]
            new_start = 8
        elif len_x[i] == 20:
            cond = listx[0:9]
            new_start = 9
    else:
        if len_x[i] == 2:
            cond = listx[new_start:new_start]
            new_start = new_start + 0
        if len_x[i] == 4:
            cond = listx[new_start:new_start+1]
            new_start = new_start + 1
        elif len_x[i] == 6:
            cond = listx[new_start:new_start+2]
            new_start = new_start + 2
        elif len_x[i] == 8:
            cond = listx[new_start:new_start+3]
            new_start = new_start + 3
        elif len_x[i] == 10:
            cond = listx[new_start:new_start+4]
            new_start = new_start + 4
        elif len_x[i] == 12:
            cond = listx[new_start:new_start+5]
            new_start = new_start + 5
        elif len_x[i] == 14:
            cond = listx[new_start:new_start+6]
            new_start = new_start + 6
        elif len_x[i] == 16:
            cond = listx[new_start:new_start+7]
            new_start = new_start + 7
        elif len_x[i] == 18:
            cond = listx[new_start:new_start+8]
            new_start = new_start + 8
        elif len_x[i] == 20:
            cond = listx[new_start:new_start+9]
            new_start = new_start + 9

    abc.append(cond)


my_dict = {}
straightline_dict = {}
for i in range(len(main_city)):  # dictionary of main_city and the cost to neighbour cities
    my_dict[main_city[i]] = abc[i]

for i in range(len(main_city)):
    # dictionary of current_city and straightline_distance
    straightline_dict[main_city[i]] = straightline_distance[i]
cost = {main_city[0]: 0}


def a_star():  # A* algorithm
    global my_dict, straightline_dict
    closed = []
    opened = [[main_city[0], straightline_distance[0]]]
    # print(opened)
    while True:
        fn = [i[1] for i in opened]
        chosen_index = fn.index(min(fn))
        # print(fn)
        node = opened[chosen_index][0]
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        # print(opened)
        if closed[-1][0] == main_city[len(main_city) - 1]:
            break
        for item in my_dict[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            cost.update({item[0]: cost[node] + item[1]})
            fn_node = cost[node] + straightline_dict[item[0]] + item[1]
            temp = [item[0], fn_node]
            # print(temp)
            opened.append(temp)
            # print(opened)
    trace_node = main_city[len(main_city) - 1]
    optimal_sequence = [main_city[len(main_city) - 1]]
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]
        if trace_node in [children[0] for children in my_dict[check_node]]:
            children_costs = [temp[1] for temp in my_dict[check_node]]
            children_nodes = [temp[0] for temp in my_dict[check_node]]
            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                optimal_sequence.append(check_node)
                trace_node = check_node
    optimal_sequence.reverse()
    return closed, optimal_sequence


if __name__ == "__main__":
    visited_nodes, optimal_nodes = a_star()
    if not optimal_nodes:
        print("NO PATH FOUND")
    else:
        for i in optimal_nodes:
            print(i, end=" -> ")
        print(" ")
        print("Total Distance:",
              visited_nodes[len(visited_nodes) - 1][1], "km")
