# 'no tenga acceso' se puede representar como una variable booleana
tiene_acceso = True
no_tiene_acceso = not tiene_acceso

# 'es falso que no tenga acceso'
es_falso_que_no_tenga_acceso = not no_tiene_acceso

# 'No es falso que no tenga acceso'
resultado_final = not es_falso_que_no_tenga_acceso

# Simplificado: not (not (not tiene_acceso)) que es lo mismo que not tiene_acceso
# Pero la frase es "No es falso que (no tenga acceso)"
# (no tenga acceso) = False (si sí tiene acceso)
# es falso que (False) = True
# No (True) = False
# La frase es confusa, la interpretación más directa es:
expresion_directa = not (not tiene_acceso)

print(f"'tiene_acceso' es: {tiene_acceso}")
print(f"El resultado de 'No es falso que no tenga acceso' es: {expresion_directa}")