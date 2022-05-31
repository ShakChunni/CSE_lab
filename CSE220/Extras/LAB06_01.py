# Utility function to swap values at two indices in the list
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Function to perform selection sort on a list
def selectionSort(A):
    for i in range(len(A) - 1):

        # find the minimum element in the unsorted sublist `A[i…n-1]`
        # and swap it with `A[i]`
        min = i

        for j in range(i + 1, len(A)):
            # if the `A[j]` element is less, then it is the new minimum
            if A[j] < A[min]:
                min = j  # update the index of minimum element

        # swap the minimum element in sublist `A[i…n-1]` with `A[i]`
        swap(A, min, i)


#if __name__ == '__main__':
A = [15,12,33,34,54,3,2,1]

selectionSort(A)

    # print the sorted list
print(A)