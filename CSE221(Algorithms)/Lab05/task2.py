import sys
import numpy as np
input_file = open('task2_input.txt', 'r')
readfile = input_file.readline()
array = [[], []]
arr1 = []
arr2 = []
for i in input_file:
    line = i
    if line == "\n":
        break
    var = list(map(str, line.split()))
    #print(var[0])
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
first_person_ending = array[1][0]
second_person_ending = array[1][1]
c = 0
count = 2
while c < len(array[0]):              
    if array[0][c] >= first_person_ending:      
        count = count + 1
        first_person_ending = array[1][c]
    elif array[0][c] >= second_person_ending:
        count = count + 1
        second_person_ending = array[1][c]
    c = c + 1
sys.stdout = open('output2.txt', 'w')
print(count)
sys.stdout.close()

