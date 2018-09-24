a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a + b > c and b + c > a and c + a > b:
    print("Трикутник існує")
else:
    print("Такого трикутника не існує")
