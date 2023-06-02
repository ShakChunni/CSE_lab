import random
import math
def alphabeta(depth, state, maximizingPlayer, list, alpha, beta):
    if depth == 3:                                  #top node reached
        return list[state]
    if maximizingPlayer:                                #alpha puring
        best = -math.inf
        for i in range(0, 2):
            val = alphabeta(depth + 1, state * 2 + i, False, list, alpha, beta)             #check korsi left side and then compared and right side
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break          
        return best
      
    else:                                   #beta puring
        best = math.inf
        for i in range(0, 2):
            val = alphabeta(depth + 1, state * 2 + i, True, list, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

if __name__ == "__main__":
    id = ("20101412")                      #original ID = 20101411 but as last 2 digits are same, changed it to 12
    total_nums = 8
    total_shuffles = 8                     #as 4th digit is 0 thus 8         
    points_needed = (id[::-1])
    points_needed = int(points_needed[0:2])     
    minimum_point = int(id[4])
    maximum_point = int(points_needed*1.5)      #last 2 digits swapped and multiplied by 1.5

#task1
    generated_nums = random.sample(range(minimum_point, maximum_point), total_nums)
    print("Task 1:")
    print("Generated 8 random points between the minimum and maximum point limits: " , generated_nums)
    print("Total points to win: ", points_needed)
    list = generated_nums
    ans = alphabeta(0, 0, True, list, -math.inf, math.inf)
    print("Achieved point by applying alpha-beta pruning :", ans)
    if ans >= points_needed:
        print("The winner is Optimus Prime")
    else:
        print("The winner is Megatron")


#task 2
    print(" ")
    print("Task 2: ")
    count = 0
    y = []
    while count < total_shuffles:
        generated_nums = random.sample(range(minimum_point, maximum_point), total_nums)
        ans = alphabeta(0, 0, True, generated_nums, -math.inf, math.inf)
        y.append(ans)
        count += 1

    print("List of all points values from each shuffles: ", y)
    print("The maximum value of all shuffles: ", max(y))
    won = 0
    for i in y:
        if i >= points_needed:
            won += 1
    print("Won", won, "times out of", total_shuffles ,"number of shuffles")