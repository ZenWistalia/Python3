#!/usr/bin/python3
import math
import cmath

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

x1 = x2 = 0

if a == 0:
    if b == 0:
        x1 = x2 = - c
    else:
        x1 = x2 = -c / b
else:
    D = b**2 - 4*a*c
    if D < 0:
        x1 = (- b + 0j * cmath.sqrt(D)) / (2 * a)
        x2 = (- b - 0j * cmath.sqrt(D)) / (2 * a)
    else:
        if D > 0:
            x1 = (-b + math.sqrt(D)) / 2 * a
            x2 = (-b - math.sqrt(D)) / 2 * a
        else:
            x1 = x2 = -b / (2 * a)

print("x1: " + str(x1))
print("x2: " + str(x2))
