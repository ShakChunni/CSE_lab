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
