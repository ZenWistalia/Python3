#!/usr/bin/python3

n = int(input('Enter n: '))
print(n and not(n & (n - 1)))
