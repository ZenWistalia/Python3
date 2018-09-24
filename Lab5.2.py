#!/usr/bin/python3

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

h = int(input("h: "))
w = int(input("w: "))

if (a <= h and b <= w) or (b <= h and c <= w) or (c <= h and a <= w):
    print(True)
elif (a <= w and b <= h) or (b <= w and c <= h) or (c <= w and a <= h):
    print(True)
else:
    print(False)
