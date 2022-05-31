#1
#n, k = list(map(int, input().split()))
#a = list(map(int, input().split()))
#total = 0
#for i in range(0, len(a)):
 #   if a[i] >= a[k-1] and a[i] > 0:
  #      total += 1
#print(total)
#2

#n = int(input())
#total = 0
#for i in range(0, n):
   # x, y, z = list(map(int, input().split()))
  #  if x + y + z >= 2:
   #     total += 1
#print(total)

#3
#m, n = list(map(int, input().split()))
#print(int(m*n/2))

#4
#n = int(input())
#final_value = 0
#for i in range(0, n):
  #  var = str(input())
   # if var[0] == '+' or var[1] == '+':
   #     final_value += 1
  #  elif var[0] == '-' or var[1] == '-':
#        final_value -= 1
#print(final_value)

#5
x = input().upper()
y = input().upper()
if x == y:
    print(0)
elif x > y:
    print(1)
elif x < y:
    print(-1)