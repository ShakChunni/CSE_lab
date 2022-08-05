import random
randomList_x = random.sample(range(-100, 100), 50)
randomList_y = random.sample(range(-100, 100), 50)


randomList_x_new = []
randomList_y_new = []

for i in randomList_x:
    randomList_x_new.append(i/100)
for i in randomList_y:
    randomList_y_new.append(i/100)

count1 = 0
count2 = 0
while count1 < 50:
    while count2 < 50:
        print(randomList_x_new[count1], randomList_y_new[count2])
        count1 += 1
        count2 += 1