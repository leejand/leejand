a = int(input("Primer número: "))
b = int(input("Segundo número: "))
if b != 0 and a % b == 0:
    print(a, "es múltiplo de", b)
else:
    print(a, "no es múltiplo de", b)