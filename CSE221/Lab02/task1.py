import sys
def best_case_bubbleSort(array):
    for i in range (len(array)):
        memory = False # I am using memory to remeber if the swap has already been done or not.
        for j in range(0, len(array)-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                memory = True # When swaping happens we are making sure to remember it.
        if memory == False:   # no swaping means that the array is already sorted so there is no need for further comparison. 
            break

input_file = open('input1.txt', 'r')
input_file = input_file.read()
sys.stdout = open('output1.txt', 'w')
input_array = input_file.split('\n')
input_array_length = int(input_array[0])

arrF = input_array[1].split()
for i in range(len(arrF)):
    arrF[i] = int(arrF[i])
best_case_bubbleSort(arrF)
for i in range(len(arrF)):
    print(arrF[i], end=" ")
sys.stdout.close()
