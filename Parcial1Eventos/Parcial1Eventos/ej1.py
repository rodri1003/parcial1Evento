cadena = "askakanasindsananadsjsdanana"
palabra_buscada = "ana"

indices_coincidencia = []

contador_coincidencias = 0

posicion_actual = 0

while True:
    indice = cadena.find(palabra_buscada, posicion_actual)
    
    if indice == -1:
        break
    
    indices_coincidencia.append(indice)
    
    contador_coincidencias += 1
    
    posicion_actual = indice + 1

print("La palabra 'ana' se repite", contador_coincidencias, "veces.")

print("Índices de coincidencia:", indices_coincidencia)
