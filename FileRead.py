import module
import math
print('The value of pi is', math.pi)

import math as m
print('The value of pi again is', m.pi)

print('Math')
print(2+3)
print(2**3)
print(3*'Deepak')
print(3/2.0)
print(3//2)

myfile = open("E:/GIT/Python/readme.txt", "r")
print "File name: ", myfile.name
c = myfile.readlines()

for line in c:
   print('Line: ' + line)
   
myfile = open("E:/GIT/Python/readme.txt", "r")
print('Entire File: \n'+myfile.read())

myfile = open("E:/GIT/Python/readme.txt", "r")
print('Only 5 Char in File: '+myfile.read(5))

print('Calling module')
print('The Add from module is ', module.add(4,5))
