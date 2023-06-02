import sys
input_file = open('task3_input.txt', 'r')
input_file = input_file.read()
input_array = input_file.split('\n')
#print(input_array)
test_case = input_array[0]
time_line = input_array[1].split()
person_line = input_array[2].split()
for i in person_line:
    x = i
word = x
person_line = list(x)
time, person = [], []
for i in range(len(time_line)):
    time.append(int(time_line[i]))
for i in range(len(person_line)):
    person.append(person_line[i])
time.sort()


jack_hours = 0
jill_hours = 0
jack_chore_list = []
c = 0
sequence = []
for i in range (len(person)):
    if person[i] == 'J':
        jack_hours = jack_hours + time[c]
        jack_chore_list.append(time[c])
        sequence.append(time[c])
        c = c + 1
    elif person[i] == 'j':
        jack_chore_list.sort()
        jack_chore_list.reverse()
        jill_hours = jill_hours + jack_chore_list[0]
        sequence.append(jack_chore_list[0])
        jack_chore_list.pop(0)

sys.stdout = open('output3.txt', 'w')
for i in range(len(sequence)):
    print(sequence[i], end="")
print(" ")
print("Jack will work for", jack_hours, "hours")
print("Jill will work for", jill_hours, "hours")
sys.stdout.close()