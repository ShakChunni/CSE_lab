import sys
def insertion_sort(array):
    for i in range(len(array)):
        current_index = array[i]
        temp = i - 1
        while temp >= 0 and current_index < array[temp]:
            array[temp + 1] = array[temp]
            temp -= 1
        array[temp + 1] = current_index

input_file = open('input3.txt', 'r')
input_file = input_file.read()
sys.stdout = open('output3.txt', 'w')
input_array = input_file.split('\n')

input_array_line1 = input_array[0].split()
input_array_line2 = input_array[1].split()
input_array_line3 = input_array[2].split()

for i in range(len(input_array_line1)):
    input_array_line1[i] = int(input_array_line1[i])
for i in range(len(input_array_line2)):
    input_array_line2[i] = int(input_array_line2[i])
for i in range(len(input_array_line3)):
    input_array_line3[i] = int(input_array_line3[i])
array = [None] * input_array_line1[0]

for i in range(input_array_line1[0]):
    array[i] = [input_array_line3[i], input_array_line2[i]]

for i in range(len(array)):
    insertion_sort(array)
array.reverse()
for i in array:
    print(i[1], end=" ")
sys.stdout.close()

