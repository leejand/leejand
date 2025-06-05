numero_entero = 20

# Proceso de conversión
texto = str(numero_entero)
flotante = float(texto)
entero_final = int(flotante)

print(f"Original (entero): {numero_entero}, tipo: {type(numero_entero)}")
print(f"A texto: '{texto}', tipo: {type(texto)}")
print(f"A flotante: {flotante}, tipo: {type(flotante)}")
print(f"De vuelta a entero: {entero_final}, tipo: {type(entero_final)}")