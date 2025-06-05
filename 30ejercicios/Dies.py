a = 15
b = 8
c = 22

# Encontrar el mayor
if a >= b and a >= c:
  mayor = a
elif b >= a and b >= c:
  mayor = b
else:
  mayor = c

print(f"El número mayor entre {a}, {b} y {c} es: {mayor}")