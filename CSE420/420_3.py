import re
regex = []
reg = []
inp1 = []
x = []
y = int(input("write number of re: "))
for i in range(0, y):
  elems = input()
  regex.append(elems)
for i in range(0, len(regex)):
  x = re.compile(regex[i])
  reg.append(x)
x = int(input("write number of strings: "))
for i in range(0, x):
  elements = input()
  inp1.append(elements)

i = 0
j = 0
while i < len(inp1):
    while j < len(reg):
        if re.match(reg[j], inp1[i]):
            print("YES", j + 1)
            break
        elif not re.match(reg[j], inp1[i]):
            j += 1
            if re.match(reg[j], inp1[i]):
                print("YES", j + 1)
                break
            elif not re.match(reg[j], inp1[i]):
                while j < len(reg):
                    j += 1
                    if j < len(reg):
                        if re.match(reg[j], inp1[i]):
                            print("YES", j + 1)
                            j += 1
                            break
                    elif j >= len(reg):        
                        print("NO", 0)
                        break
    i += 1
    j = 0
            