#!/usr/bin/python3

line = input("Enter text: ")
k = int(input("Enter k: "))

newStr = ""
if k>0:
    for i in range(-k,len(line) - k) :
        newStr+=line[i]
elif k<0:
    for i in range(0,len(line)):
        newStr+=line[i+k]
else:
    newStr = line

print("Result: " + newStr)
