#!/usr/bin/python3

mass = int(input("Enter mas(kg): "))
height = int(input("Enter height(m): "))

bmi = mass / (height**2)

print("BMI: " + str(bmi))
