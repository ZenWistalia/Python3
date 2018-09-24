#!/usr/bin/python3

import random

print("1. Камінь\n")
print("2. Ножиці\n")
print("3. Папір\n")
UserChose = int(input("Ваш вибір: "))

PcChose = random.randrange(1, 3)
print("Комп'ютер вибрав: " + str(PcChose))

if UserChose > PcChose or (UserChose == 3 and PcChose == 1):
    print("Комп'ютер виграв")
elif UserChose == PcChose:
    print("Нічия")
else:
    print("Користувач виграв")
