import sys
import numpy as np
input_file = open('task1_input.txt', 'r')
readfile = input_file.readline()
test_case = int(readfile)
array = [[], []]
arr1 = []
arr2 = []
for i in input_file:
    line = i
    if line == "\n":
        break
    var = list(map(str, line.split()))
    start = int(var[0])
    end = int(var[1])
    arr1.append(start)
    arr2.append(end)
arr = zip(arr2, arr1)
sorted_arr = sorted(arr)

for i in range(0, len(sorted_arr)):
    starti_time = sorted_arr[i][1]
    endi_time = sorted_arr[i][0]
    array[0].append(starti_time)
    array[1].append(endi_time)

f = array[1][0]
c = 0
count = 1
leo = []
messi = []
leo.append(f)
messi.append(array[0][c])
while c < test_case:             
    if array[0][c] >= f:      
        count = count + 1
        f = array[1][c]
        leo.append(f)
        messi.append(array[0][c])  
    c = c + 1

sys.stdout = open('output1.txt', 'w')
print(count)
for i in range(len(messi)):
      print(messi[i], leo[i])
sys.stdout.close()