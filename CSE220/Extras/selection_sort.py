def selection_sort(array, i, length):
    min_index = i
    for j in range(i+1, length):
        if array[j] < array[min_index]:
            min_index = j
    temporary = array[min_index]
    array[min_index] = array[i]
    array[i] = temporary
    if i+1 < length:
        selection_sort(array, i+1, length)

array=[15,57,-15,177,44,-8874,4,-12,33,34,54,3,2,1]
selection_sort(array, 0, len(array))
print(array)