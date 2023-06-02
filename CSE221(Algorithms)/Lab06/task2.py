import sys
def lcs2(X, Y, Z):
	m = (len(X) + 1)
	n = (len(Y) + 1)
	o = (len(Z) + 1)
	var = [[[0 for i in range(o)] for j in range(n)] for k in range(m)]
	for i in range(1, m):
		for j in range(1, n):
			for k in range(1, o):
				if (i == 0 or j == 0 or k == 0):
					var[i][j][k] = 0
				elif (X[i - 1] == Y[j - 1]) and X[i - 1] == Z[k - 1]:
					var[i][j][k] = 1 + var[i - 1][j - 1][k - 1] 
				else:
					var[i][j][k] = max(var[i - 1][j][k], var[i][j - 1][k], var[i][j][k - 1])
	return var[m - 1][n - 1][o - 1] 


input_file = open('task2_input.txt', 'r')
input_file = input_file.read()
input_array = input_file.split('\n')
first_string = input_array[0]
second_string = input_array[1]
third_string = input_array[2]
longest_common_subsequence = lcs2(first_string, second_string, third_string)
sys.stdout = open('output2.txt', 'w')
print(longest_common_subsequence)
sys.stdout.close()