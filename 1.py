a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

while b != 0:
    qoldiq = a % b
    a = b
    b = qoldiq

print("EKUB =", a)
