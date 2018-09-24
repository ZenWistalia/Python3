#!/usr/bin/python3

zero_fahrenheit = 32
one_fahrenheit = (212-32)/100
fahrenheit = int(input("Enter fahrenheit: "))
celsius = (fahrenheit - zero_fahrenheit) / one_fahrenheit
print("Celsius: " + str(celsius))
