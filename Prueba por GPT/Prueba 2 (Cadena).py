def contar_vocales(cadena):
    contador=0
    vocales='aeiou'
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return(contador)
cadena= "No se que escribir"
resultado= contar_vocales(cadena)
print("La cadena tiene ", resultado)
