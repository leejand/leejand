contrasena = "claveSegura123"

# Verificar longitud
longitud_correcta = len(contrasena) > 8
# Verificar si tiene al menos un número
tiene_numero = any(c.isdigit() for c in contrasena)

# Comprobar si es segura
es_segura = longitud_correcta and tiene_numero

print(f"¿La contraseña es segura?: {es_segura}")