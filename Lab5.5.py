#!/usr/bin/python3

n = int(input("N: "))

if n == 2 or n == 3:
    print(True)
if n < 2 or n % 2 == 0:
    print(False)
if n < 9:
    print(True)
if n % 3 == 0:
    print(False)
r = int(n**0.5)
f = 5
while f <= r:
    if n % f == 0:
        print(False)
    if n % (f+2) == 0:
        print(False)
    f += 6
print(True)
