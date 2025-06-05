temperatura = 40
humedad = 85

# Verificar si se activa la alarma
activar_alarma = (temperatura < 0 or temperatura > 38) and humedad > 80

print(f"¿Activar alarma?: {activar_alarma}")