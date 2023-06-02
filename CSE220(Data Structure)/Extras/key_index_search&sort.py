class KeyIndex:
    k = []

    def __init__(self, a):
        largest_element = a[0]
        smallest_element = a[0]
        for i in range(0, len(a)):
            if a[i] < smallest_element:
                smallest_element = a[i]
        if smallest_element < 0:
            smallest_element = smallest_element * -1
            for i in range(0, len(a)):
                a[i] = a[i] + smallest_element
        else:
            smallest_element = 0
        for i in range(0, len(a)):
            if a[i] > largest_element:
                largest_element = a[i]
        size_of_k = largest_element + 1
        KeyIndex.k = [0] * size_of_k
        for i in range(0, len(a)):
            KeyIndex.k[a[i]] = KeyIndex.k[a[i]] + 1
        self.smallest_element = smallest_element
        self.a = a

    def search(self, value):
        value = value + self.smallest_element
        for i in range(0, len(KeyIndex.k)):
            if value >= len(KeyIndex.k) or value < 0:
                return False
            elif KeyIndex.k[value] != 0:
                return True
            else:
                return False

    def sort(self):
        count = 0
        for i in range(0, len(KeyIndex.k)):
            while KeyIndex.k[i] > 0:
                self.a[count] = i - self.smallest_element
                count += 1
                KeyIndex.k[i] = KeyIndex.k[i] - 1
        return self.a


class Tester:
    array = KeyIndex([-4, -2, 0, 12, 3, 4, -7, 4])
    print(array.search(11))
    print(array.sort())
