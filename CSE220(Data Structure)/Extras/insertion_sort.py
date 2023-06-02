def insertion_sort(array,length):
    if length > 1:
        insertion_sort(array, length - 1)
        last_element = array[length-1]
        next_element = length-2
        while next_element >= 0 and array[next_element] > last_element:
            array[next_element+1] = array[next_element]
            next_element = next_element - 1
        array[next_element+1] = last_element

array=[15,57,-15,177,44,-8874,4,-12,33,34,54,3,2,1]
length = len(array)
insertion_sort(array,length)
print(array)



