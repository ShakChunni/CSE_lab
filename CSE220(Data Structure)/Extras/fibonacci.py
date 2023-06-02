temporary = {}
def fib(var):
    if var in temporary:
        return temporary[var]
    elif var in range (1,3):
        new_var = 1
    elif var > 2:
        new_var = fib(var - 1) + fib(var - 2)
    else:
        return "Error: Wrong Input!"
    temporary[var] = new_var
    return new_var

for i in range(1,1000):
    print(fib(i))
