#01


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


#02


class HashTable:
    def __init__(self):
        self.length = 9
        self.array = [None] * self.length

    def hash_function(self, string):
        consonants = 0
        sum_of_numbers = 0
        vowels = 0
        for i in string:
            if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
                vowels += 1
            elif (i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or
                    i == '5' or i == '6' or i == '7' or i == '8' or i == '9'):
                x = int(i)
                sum_of_numbers = sum_of_numbers + x
            else:
                consonants += 1
        return (consonants * 24 + sum_of_numbers) % 9

    def insert(self, element):
        hash_key = self.hash_function(element)
        index = hash_key
        while self.array[index] is not None:        # Linear Probing
            index = (index + 1) % self.length
        self.array[index] = element


class Tester:
    ht = HashTable()
    list = ["CSE220", "STA201", "STA201", "ST1E89B8A32", "CSE220", "CSE220",
            "ST1E89B8A32", "ST1E89B8A32", "ST1E89B8A32"]
    for i in range(0, len(list)):
        ht.insert(list[i])
    print(ht.array)
