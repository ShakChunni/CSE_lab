# 7
def binary_search(array, right_most_value, wanted_value):
    left_index = 0
    current_index = right_most_value - 1
    while left_index <= current_index:
        mid_value = int((left_index + current_index)/2)
        if array[mid_value] <= wanted_value:
            left_index = mid_value + 1
        else:
            current_index = mid_value - 1
    return current_index


def count(array1, array2):
    for i in range(len(array2)):
        nums = binary_search(array1, len(array1), array2[i])
        print(nums + 1, end=" ")


test_array1 = [1, 1, 2, 2, 5]
test_array2 = [3, 1, 4, 1, 5]
count(test_array1, test_array2)
