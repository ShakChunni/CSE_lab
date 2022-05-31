from os import X_OK
import sys
def lcs1(X, Y):
    m = (len(X) + 1)
    n = (len(Y) + 1)
    var = [[0]*(n) for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            if X[i - 1] == Y[j - 1]:
                var[i][j] = var[i - 1][j - 1] + 1
            else:
                var[i][j] = max(var[i - 1][j],var[i][j - 1])
    length = var[m - 1][n - 1]
    array = [None] * (length + 1)
    array[length] = None
    i = m - 1
    j = n - 1
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            array[length - 1] = X[i - 1]
            i = i - 1
            j = j - 1
            length = length - 1
        elif var[i-1][j] > var[i][j-1]:
            i = i - 1
        else:
            j = j - 1
    return(array, var[m-1][n-1])


input_file = open('input1.txt', 'r')
input_file = input_file.read()
input_array = input_file.split('\n')
no_of_zones = int(input_array[0])
zone_sequence = input_array[1]
prediction_sequence = input_array[2]
z = lcs1(zone_sequence, prediction_sequence)
z1 = z[0]
print(z)
array = []
for i in range(len(z1)):
    if z1[i] == "Y":
        array.append("Yasnaya")
    elif z1[i] == "P":
        array.append("Pochinki")
    elif z1[i] == "S":
        array.append("School")
    elif z1[i] == "R":
        array.append("Rozhok")
    elif z1[i] == "F":
        array.append("Farm")
    elif z1[i] == "M":
        array.append("Mylta")
    elif z1[i] == "H":
        array.append("Shelter")
    elif z1[i] == "I":
        array.append("Prison")        
#sys.stdout = open('output1.txt', 'w')
#for i in range(len(array)):
#    print(array[i], end=" ")
#print("")
#print("Correctness of prediction:", int((z[1]/no_of_zones)*100), end="%")
#sys.stdout.close()
