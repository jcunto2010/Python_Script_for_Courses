#Para encontrar números dentro de un texto y sumarlos

import re

name = input("Enter file:")
if len(name) < 1:
    name = "assigment.txt"

handle = open(name)
acu = 0
numlist = list()
for line in handle:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    #print(stuff)
    if len(stuff) <1:
        continue
    #print(stuff)
    num = [int(x) for x in stuff]
    #print(num)
    for num in stuff:
        numlist.append(num)
    val = [int(y) for y in numlist]
    acu = sum(val)
print(acu)








