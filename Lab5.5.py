#!/usr/bin/python3

n = int(input("N: "))

if n == 1:
        print("Число не просте\n")
else:
    for x in range(2, n):
        if n % x == 0:
            print("Число не просте\n")
            break
    else:
        print("Число просте\n")
