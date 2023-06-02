# -*- coding: utf-8 -*-
"""'20101327_F_M_Ashfaq_02_Floating_Point_Representation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1guGjFPyZBbkjyblAGz9Op7IXaKjeolbJ

Make sure you remove `raise NotImplementedError()` and fill in any place that says `# YOUR CODE HERE`, as well as your `NAME`, `ID`, and `LAB_SECTION` below:
"""

NAME = "F.M. Ashfaq"
ID = "20101327"
SECTION = "02"

"""---

# Floating Point Representation

## 8 bit Floating Point Representation

We will implement an 8 bit Floating point number system in this part, where First bit is a sign bit, next three bits are exponents,
and the rest 4 bits are mantissas (significands).

Numbers are divided into two categories: normals and subnormals.

For normals the encoding is:
\begin{equation}
(-1)^{sign} \times 2^{(e-3)} \times 1.fraction
\end{equation}
For subnormals the encoding is:
\begin{equation}
(-1)^{sign} \times 2^{(1-3)} \times 0.fraction
\end{equation}

Example:
\begin{aligned}
    0 001 0000 &= 2^{(1-3)} \times 1.0 = 0.25\\
    0 010 0000 &= 2^{(2-3)} \times 1.0 = 0.5\\
    0 011 0000 &= 2^{(3-3)} \times 1.0 = 1.0\\
    0 011 0100 &= 2^{(3-3)} \times 1.25 = 1.25
\end{aligned}

If the exponent is 0 then the number is considered subnormal.

Example:
\begin{aligned}
    0 000 0000 &= 2^{-2} \times 0   = 0.0\\
    0 000 1000 &= 2^{-2} \times 0.5 = 0.125\\
    0 000 1100 &= 2^{-2} \times 0.75 = 0.1875
\end{aligned}

If the exponent is 7 then and mantissa is zero then the number is 
considered infinity (inf), otherwise it is not-a-number (nan).

Example:
\begin{aligned}
    0 111 0000 &= +\infty\\
    1 111 0000 &= -\infty\\
    X 111 XXXX &= NaN
\end{aligned}

### Instructions
In this task, you need to implement the `Float8()` class. Some parts of the class are already written for you. You only need to modify `__init__(self, bitstring)` and `calculate_value(self)` fuctions, where it says `# YOUR CODE HERE`. You may ignore `raise NotImplementedError()`.
"""

import math
import itertools
import matplotlib.pyplot as plt

class Float8():
    
    def __init__(self, bitstring):
        '''Constructor
        takes a 8-bit string of 0's and 1's as input and stores the sub-strings
        accordingly.
        Usage: Float8('00011110')
        '''
        
        # Make sure the input consists of exactly 8-bits.
        assert(len(bitstring)==8)
        
        # Assign the sign bit
        self.sign = bitstring[0]
        

        # Assign the exponent part
        self.exponent = bitstring[1:4]

        

        # Assign the mantissa
        self.mantissa = bitstring[4:]
        
        # YOUR CODE HERE
        #raise NotImplementedError()
        
        self.val = self.calculate_value()
        
    def __str__(self):
        return f'Sign bit value: {self.sign}\n' + \
            f'Exponent value: {self.exponent}\n' + \
            f'Mantissa value: {self.mantissa}\n' + \
            f'Floating value: {self.val}\n'
    
    def tobitstring(self):
        return self.sign + self.exponent + self.mantissa
    
    def toformattedstring(self):
        return ' '.join([self.sign, self.exponent, self.mantissa])
    
    def calculate_value(self):
        '''Calculate the value of the number from bits'''
        
        # Initialize with zero
        val = 0.0
        
        # YOUR CODE HERE
        if self.exponent == '111':  #7
            if self.mantissa == '0000':
                val = math.inf
            else:
                val = math.nan
        elif self.exponent == '000':
            val = 0.0
            for exp, bit in enumerate(self.mantissa):
                  val += int(bit) * 2**(-exp - 1) #fraction er decimal hishab kore formula te boshay dicche(binary te . er pore)
            val *= 2**(1-3)  #multiply kore disey
        else:
            val = 1.0 #because normal form e 1.fraction
            for exp, bit in enumerate(self.mantissa):
                val += int(bit)* 2**(-exp - 1)  #mantisa ta hishab kortesey, 1*2^-1, 1*2^-2.....
            exp = 0.0
            for e, bit in enumerate(reversed(self.exponent)):  #
                exp += int(bit) * 2**(e)  #exponent normal, tai ulta korsey, 0*2^0
            val *= 2**(exp - 3)
        if self.sign == '0':
            val *= (-1)**0 
        if self.sign == '1':
            val *= (-1)**(1) 
        #raise NotImplementedError()
        
        return val

'''28 test cases for 8-bit floating points'''
import numpy as np

data = [ '00000000', '00000001', '00001001', '00010000',
         '00010001', '00011000', '00011011', '00100000',
         '00101101', '00110000', '00110101', '01000011',
         '01000000', '01010000', '01011100', '01100000',
         '01110111', '01110000', '10000000', '10000001',
         '11110001', '11110000', '10110001', '10111101',
         '11100000', '11101011', '11010000', '11000000']
results = ['(0, 1)', '(1, 64)', '(9, 64)', '(1, 4)', '(17, 64)', '(3, 8)', '(27, 64)',
          '(1, 2)', '(29, 32)', '(1, 1)', '(21, 16)', '(19, 8)', '(2, 1)', '(4, 1)',
          '(7, 1)', '(8, 1)', 'nan', 'inf', '(0, 1)', '(-1, 64)', 'nan', '-inf',
          '(-17, 16)', '(-29, 16)', '(-8, 1)', '(-27, 2)', '(-4, 1)', '(-2, 1)']

test = [Float8(x).val for x in data]

for index in range(len(test)):
    d = test[index]
    try:
        test[index] = str(d.as_integer_ratio())
    except Exception:
        test[index] = str(d)

np.testing.assert_equal(np.array(test), np.array(results))
print('28 out of 28 outputs matched for 8-bit floating points')

"""## 16 Bit Floating Point Representation

Over here, we will implement a 16 bit Floating point number system,
where the first bit is a sign bit, next four bits are exponents,
and the rest 11 bits are mantissas (significands).

Numbers are divided into two categories: normals and subnormals.

For normals the encoding is:
\begin{equation}
(-1)^{sign} \times 2^{(e-7)} \times 1.fraction
\end{equation}
For subnormals the encoding is:
\begin{equation}
(-1)^{sign} \times 2^{(1-7)} \times 0.fraction
\end{equation}

Example:
\begin{aligned}
    0 0101 00000000000 &= 2^{(5-7)} \times 1.0  = 0.25\\
    0 0110 00000000000 &= 2^{(6-7)} \times 1.0  = 0.5\\
    0 0111 00000000000 &= 2^{(3-7)} \times 1.0  = 1.0\\
    0 0111 01000000000 &= 2^{(3-7)} \times 1.25 = 1.25
\end{aligned}

If the exponent is 0 then the number is considered subnormal.

Example:
\begin{aligned}
    0 0000 00000000000 &= 2^{-6} \times 0    = +0.0\\
    0 0000 10000000000 &= 2^{-6} \times 0.5  = +0.0078125\\
    0 0000 11000000000 &= 2^{-6} \times 0.75 = +0.01171875
\end{aligned}

If the exponent is 15 (all 1's) then and mantissa is zero then the number is considered infinity (inf), otherwise it is not-a-number (nan).
    
Example:
\begin{aligned}
    0 1111 00000000000 &= +\infty\\
    1 1111 00000000000 &= -\infty\\
    X 1111 XXXXXXXXXXX &= NaN
\end{aligned}

### Instructions
In this task, you need to implement the `Float16()` class. Some parts of the class are already written for you. You only need to modify `__init__(self, bitstring)` and `calculate_value(self)` fuctions, where it says `# YOUR CODE HERE`. You may ignore `raise NotImplementedError()`.
"""

class Float16():
    

    def __init__(self, bitstring):
        '''Constructor
        takes a 16-bit string of 0's and 1's as input and stores the sub-strings
        accordingly.
        Usage: Float16('0001111000011110')
        '''

        # Make sure the input consists of exactly 16-bits.
        assert(len(bitstring)==16)

        # Assign the sign bit
        self.sign = bitstring[0]
        

        # Assign the exponent part
        self.exponent = bitstring[1:5]
        

        # Assign the mantissa
        self.mantissa = bitstring[5:]
        
        # YOUR CODE HERE
        #raise NotImplementedError()

        self.val = self.calculate_value()
        
    def __str__(self):
        return f'Sign bit value: {self.sign}\n' + \
            f'Exponent value: {self.exponent}\n' + \
            f'Mantissa value: {self.mantissa}\n' + \
            f'Floating value: {self.val}\n'
    
    def tobitstring(self):
        return self.sign + self.exponent + self.mantissa
    
    def toformattedstring(self):
        return ' '.join([self.sign, self.exponent, self.mantissa])
    
    def calculate_value(self):
        '''Calculate the value of the number from bits'''

        # Initialize with zero
        val = 0.0
        if self.exponent == '1111':
            if self.mantissa == '00000000000':
                val = math.inf
            else:
                val = math.nan
        elif self.exponent == '0000':
             val = 0.0
             for exp, bit in enumerate(self.mantissa):
                 val += int(bit) * 2**(-exp - 1)            
             val *= 2**(1 - 7) 
        else:
            val = 1.0
            for exp, bit in enumerate(self.mantissa):
                val += int(bit) * 2**(-exp - 1)
            exp = 0.0
            for e, bit in enumerate(reversed(self.exponent)):
                exp += int(bit) * 2**(e)
            val *= 2**(exp - 7)
        if self.sign == '0':
            val *= (-1)**0 
        else:
            val *= (-1)**1
        
        # YOUR CODE HERE
        #raise NotImplementedError()

        return val

'''28 test cases for 16-bit floating points'''
data = [ '0011100000000010', '0100000000000000', '1100000000000000', '0100010000000000',
         '1100010000000000', '0100100000000000', '1100100000000000', '0100101000000000',
         '1100101000000000', '0100110000000000', '1100110000000000', '0101101110000000',
         '0010010000000000', '0000000000000001', '0000011111111111', '0000100000000000',
         '0111011111111111', '0000000000000000', '1000000000000000', '0111100000000000',
         '1111100000000000', '0111100000000001', '0111110000000001', '0111111111111111',
         '0010101010101011', '0100010010010001', '0011100000000000', '0011100000000001']
results = ['(1025, 1024)', '(2, 1)', '(-2, 1)', '(3, 1)', '(-3, 1)', '(4, 1)', '(-4, 1)',
           '(5, 1)', '(-5, 1)', '(6, 1)', '(-6, 1)', '(23, 1)', '(3, 16)', '(1, 131072)',
           '(2047, 131072)', '(1, 64)', '(4095, 16)', '(0, 1)', '(0, 1)', 'inf', '-inf',
           'nan', 'nan', 'nan', '(2731, 8192)', '(3217, 1024)', '(1, 1)', '(2049, 2048)']

test = [Float16(x).val for x in data]

for index in range(len(test)):
    d = test[index]
    try:
        test[index] = str(d.as_integer_ratio())
    except Exception:
        test[index] = str(d)

np.testing.assert_equal(np.array(test), np.array(results))
print('28 out of 28 outputs matched for 16-bit floating points')