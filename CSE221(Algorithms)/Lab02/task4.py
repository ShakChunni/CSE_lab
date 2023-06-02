import sys
def merge(array, left, right, mid):
    temp1 = mid - left + 1
    temp2 = right - mid
    temp_array1 = [0] * temp1
    temp_array2 = [0] * temp2
    for i in range(temp1):
        temp_array1[i] = array[left + i]
    for i in range(temp2):
        temp_array2[i] = array[mid + 1 + i]
    x, y = 0, 0
    z = left
    while x < temp1 and y < temp2:
        if temp_array1[x] <= temp_array2[y]:
            array[z] = temp_array1[x]
            x += 1
        else:
            array[z] = temp_array2[y]
            y += 1
        z += 1
    while x < temp1:
        array[z] = temp_array1[x]
        x += 1
        z += 1
    while y < temp2:
        array[z] = temp_array2[y]
        y += 1
        z += 1

def merge_sort(array, left, right):
    if left < right:
        mid = (left+(right-1))//2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, right, mid)
 

input_file = open('input4.txt', 'r')
input_file = input_file.read()
sys.stdout = open('output4.txt', 'w')
input_array = input_file.split('\n')

input_array_line1 = input_array[0].split()
input_array_line2 = input_array[1].split()
for i in range(len(input_array_line1)):
    input_array_line1[i] = int(input_array_line1[i])

for i in range(len(input_array_line2)):
    input_array_line2[i] = int(input_array_line2[i])
length_of_array = len(input_array_line2)
merge_sort(input_array_line2, 0, length_of_array - 1)
for i in range(length_of_array):
    print(input_array_line2[i], end=" ")
sys.stdout.close()