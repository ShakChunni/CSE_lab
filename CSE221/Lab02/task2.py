import sys
import numpy as np
def selection_sort(array):
    for i in range(len(array)):
        minimum_index = i
        for j in range(i + 1, len(array)):
            if array[minimum_index] > array[j]:
                minimum_index = j
        array[i], array[minimum_index] = array[minimum_index], array[i]

input_file = open('input2.txt', 'r')
input_file = input_file.read()
sys.stdout = open('output2.txt', 'w')
input_array = input_file.split('\n')

input_array_line1 = input_array[0].split()
input_array_line2 = input_array[1].split()

for i in range(len(input_array_line1)):
    input_array_line1[i] = int(input_array_line1[i])

for i in range(len(input_array_line2)):
    input_array_line2[i] = int(input_array_line2[i])
selection_sort(input_array_line2)

 
for i in range(input_array_line1[1]):
    print(input_array_line2[i], end=" ")
sys.stdout.close()
