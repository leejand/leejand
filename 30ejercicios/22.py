tiene_pase_vip = False
pago_entrada = True
esta_ebrio = False

# Verificar si puede entrar
puede_entrar = tiene_pase_vip or (pago_entrada and not esta_ebrio)

print(f"¿Puede entrar?: {puede_entrar}")