def binary_search(array, wanted_value,left_most_index, right_most_index):
    if left_most_index <= right_most_index:
        mid_value = (left_most_index + right_most_index) // 2
        if wanted_value == array[mid_value]:
            return mid_value
        elif wanted_value < array[mid_value]:
            return binary_search(array, wanted_value,left_most_index, mid_value-1)
        elif wanted_value > array[mid_value]:
            return binary_search(array, wanted_value, mid_value+1, right_most_index)
        else:
            return "Value not inside the array!"
    else:
        return "Value not inside the array!"
array = [3,6,12,14,15,18,87,120,225,244,445]
wanted_value = 15
print(binary_search(array, wanted_value, 0, len(array)-1))

