import random
my_id = "20101344"
if my_id[3] == 0:
    amountOfShuffle = 8
mini = int(my_id[4])
win = 44                                    
maxi = int(win*1.5)



def minimax(depth, nodeIndex, maximizingPlayer,
			values, alpha, beta):

	# Terminating condition. i.e
	# leaf node is reached
	if depth == 3:
		return values[nodeIndex]

	if maximizingPlayer is False:
		ans = 1000000000000000000000000000000000000
		for i in range(2):
		
			val = minimax(depth + 1, nodeIndex * 2 + i,
							True, values, alpha, beta)
			ans = min(ans, val)
			beta = min(beta, ans)

			# Alpha Beta Pruning
			if beta <= alpha:
				break
		
		return ans
	
	else:
		ans = -1000000000000000000000000000000000000

		# Recur for left and right children
		for i in range(2):
			
			val = minimax(depth + 1, nodeIndex * 2 + i,
						False, values, alpha, beta)
			ans = max(ans, val)
			alpha = max(alpha, ans)

			# Alpha Beta Pruning
			if beta <= alpha:
				break
		
		return ans

	

#eikhane change korbi, eigula shob output er..                  #min = minimum num, max = maximum number, win= joto lagbey jitar jonne, shuffle_no = 8, 2nd tay lagbey

print("The optimal value is :", minimax(0, 0, True, random.sample(range(mini, maxi), 8), -1000000000000000000000000000000000000, 1000000000000000000000000000000000000))
	

