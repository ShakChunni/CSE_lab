# Sorry sir, could not figure out a way to split the inputs from a text file to make it work. 
# I tried without the text file and it works.
# Again, I sincierly apologize for not being able to do it with the input file as my conception is still lacking :(.


# input A

N = int(input("Enter the number of rows & collums: "))
row_1 = N
col_1 = N
A = []
print("Enter the values for A as rows: ")
for i in range(0, row_1):
    temp = []
    for j in range(0, col_1):
        temp.append(int(input()))
    A.append(temp)

# input B

row_2 = N
col_2 = N
B = []
print("Enter the values for B as rows: ")
for i_1 in range(0, row_2):
    temp_2 = []
    for j_1 in range(0, col_2):
        temp_2.append(int(input()))
    B.append(temp_2)

# result

row_3 = row_1
col_3 = col_2
C = []
for i_2 in range(0, row_3):
    temp_3 = []
    for j_2 in range(0, col_3):
        temp_3.append(0)
    C.append(temp_3)

# multiplication

for i_fin in range(0, len(A)):
    for j_fin in range(0, len(B[0])):
        for x in range(len(B)):
            C[i_fin][j_fin] += A[i_fin][x] * B[x][j_fin]

for x_fin in C:
    print(x_fin)
