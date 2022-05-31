# 5
def print_space(space):
    if space == 0:
        return
    else:
        print(" ", end=" ")
    print_space(space - 1)


def print_row(var1, var2):
    if var1 == 0:
        return
    else:
        print(var2 - (var1 - 1), end="")
    print_row(var1 - 1, var2)


def print_pattern(var3, var4):
    if var3 == 0:
        return
    else:
       # print_space(var3 - 1)  # ei line ta comment kore dile 5(a) ashbe
        print_row(var4 - var3 + 1, var4 - var3 + 1)
        print(" ")
        print_pattern(var3 - 1, var4)


print_pattern(5, 5)
