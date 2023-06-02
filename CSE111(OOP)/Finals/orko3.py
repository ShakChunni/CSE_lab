#q1

ch_limit=int(input("Enter max number in series\n"))
series=1
n=0
x=False
my_dict={}
while series<=ch_limit:
    if n!=0:
        my_dict[n]=series
    n+=1
    series=int((2*n * (2*n- 1))/2)
my_dict_valueCheck=int(input("Enter a integer to check if it's in series\n"))
print(my_dict)
for i in my_dict.keys():
    if my_dict[i]==my_dict_valueCheck:
        print("Key:",i,",Value:",my_dict[i],sep=(""))
        x=True
if x==False:
    print("no such value exists")