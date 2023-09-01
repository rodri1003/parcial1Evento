palabra_base = input("Ingrese una palabra base: ")

longitud_lista = int(input("Ingrese la longitud de la lista: "))

lista_palabras = []

for i in range(longitud_lista):
    palabra = input(f"Ingrese la palabra {i + 1}: ")
    lista_palabras.append(palabra)

acronimos = []
for palabra in lista_palabras:
    if len(palabra) == len(palabra_base):
        es_acronimo = all(letra_base.lower() == letra.lower() for letra_base, letra in zip(palabra_base, palabra))
        if es_acronimo:
            acronimos.append(palabra)

if acronimos:
    print("Las palabras que son acrónimos de", palabra_base, "son:")
    for acronimo in acronimos:
        print(acronimo)
else:
    print("No se encontraron acrónimos de", palabra_base, "en la lista.")
