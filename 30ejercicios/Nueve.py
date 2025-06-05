n = 7
print(f"Número original: {n}")

if n % 2 == 0:
  # Es par, sumar 1
  n += 1
else:
  # Es impar, restar 1
  n -= 1

print(f"Número modificado: {n}")