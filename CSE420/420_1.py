import math
import re
import sys
input_file = open('input.txt', 'r')
input_file = input_file.read()
y = input_file.split()


java_keywords = ['abstract','continue',	'for','new','switch',
'assert***','default','goto*','package','synchronized',
'boolean','do','if','private' ,'this',
'break','double','implements','protected','throw',
'byte',	'else',	'import',	'public',	'throws',
'case',	'enum****',	'instanceof',	'return',	'transient',
'catch','extends',	'int',	'short','try',
'char',	'final',	'interface',	'static',	'void',
'class',	'finally',	'long',	'strictfp**',	'volatile',
'const*',	'float',	'native',	'super',	'while']
java_logical_ops = ['==', '!=', '>', '<', '>=', '<=', '&&', '!!', '!']
java_arth_ops = ['=', '+', '-', '*', '/', '+=', '-=', '*=', '/=', '%=', '&=', '|=', '^=', '>>=', '<<=']
regex_albets = re.compile("[A-Za-z]+")
regex_nums = re.compile("[+-]?([0-9]*[.])?[0-9]+")

keywords = []
identifiers = []
numbers = []
math_ops = []
logical_ops = []
others = []
for i in range(0, len(y)):
    if y[i] in java_keywords and y[i] not in keywords:
        keywords.append(y[i]) 
    elif y[i] in java_arth_ops and y[i] not in math_ops:
        math_ops.append(y[i])
    elif y[i] in java_logical_ops and y[i] not in logical_ops:
        logical_ops.append(y[i])
    elif regex_albets.fullmatch(y[i]) is not None and y[i] not in java_keywords and y[i] not in identifiers:
        identifiers.append(y[i])
    elif regex_nums.fullmatch(y[i]) is not None and y[i] not in numbers:
        numbers.append(y[i])
    elif y[i] not in java_keywords and y[i] not in identifiers and y[i] not in numbers and y[i] not in others and y[i] not in logical_ops and y[i] not in math_ops:
        others.append(y[i])

print("keywords: ", ', '.join(keywords))
print("Identifiers: ", ', '.join(identifiers))
print("Math Operators: ", ', '.join(math_ops))
print("Logical Operators: ", ', '.join(logical_ops))
print("Numerical Values: ", ', '.join(numbers))
print("Others: ", ' '.join(others))
