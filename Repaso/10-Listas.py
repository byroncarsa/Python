# INDEXACION
# numeros = [2, 4, 6, 1, 2]

# print(numeros) # Imprimir una lista
# print(numeros[1]) # Imprimir un elementos
# numeros[0] = 122 # Cambiar numero de lista
# numeros[1] = numeros[0]


# METODOS
# numeros = [2, 4, 6, 1, 2]

# Numero de elementos de la lista
# print("Longitud de la lista:", len(numeros))

# Eliminando un elemento
# del numeros[0]
# print(numeros)

# Eliminando con rebanadas
# del numeros[0:2]
# print(numeros)

# Eliminando todos los elementos
# del numeros[:]
# print(numeros)

# Eliminando la lista
# del numeros
# print(numeros)


# BLUCLE FOR
# Lista vacia
# lista = []

# For con len
# lista = []
# for i in range(5):
#     lista.append(i + 1)
# print(lista)

# For con len
# lista = [2, 3, 2, 3, 2, 3]
# total = 0

# for i in range(len(lista)):
#     total += lista[i]
# print(total)

# For in
# lista = [2, 3, 2, 3, 2, 3]
# total = 0

# for i in lista:
#     total += i
# print(total)


# REVERTIR ORDEN
# Pocos elementos
# lista = [10, 1, 8, 3, 5]
# lista[0], lista[4] = lista[4], lista[0]
# lista[1], lista[3] = lista[3], lista[1]
# print(lista)

# Muchos elementos
# lista = [10, 1, 8, 3, 5]
# for i in range(len(lista) // 2):
#     lista[i], lista[len(lista) - i - 1] = lista[len(lista) - i - 1], lista[i]
# print(lista)


# ORDENAMIENTO
# Ordenamiento burbuja
# lista = [8, 10, 6, 2, 4] 

# for i in range(len(lista) - 1):
#     if lista[i] > lista[i + 1]:
#         lista[i], lista[i + 1] = lista[i + 1], lista[i]
# print(lista)

# Sort
# lista = [8, 10, 6, 2, 4] 
# lista.sort()
# print(lista)

# Reverse
# lista = [8, 10, 6, 2, 4] 
# lista.reverse()
# print(lista)


# LA VIDA DE LAS LISTAS
# Asignacion de lista
# lista = [1]
# lista_copia = lista
# lista_copia[0] = 5
# print(lista) 
# print(lista_copia) 

# Rebanadas
# lista = [1,3,5]
# lista_copia = lista[:] # Copia todo
# lista2 = lista[0:1] # No cuenta el ultimo elemento
# print(lista_copia)
# print(lista2)


# OPERADORES IN Y NOT IN
# lista = [1, 4, 7, 9] 
# print(4 in lista) # Verificar si un elemnto esta en la lista
# print(3 not in lista) # Verificar si un elemnto no esta en la lista


# LABORATORIO 1
# hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# # Paso 1: escribe una línea de código que solicite al usuario
# # reemplazar el número de en medio con un número entero ingresado por el usuario.
# num = int(input("Ingresa un unmero entero: "))

# indice = len(hat_list) // 2

# hat_list[indice] = num

# # Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
# del(hat_list[len(hat_list) - 1])

# # Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
# print(len(hat_list))


# LABORATORIO 2
# paso 1
# beatles = []
# print("Paso 1:", beatles)

# # paso 2
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Paso 2:", beatles)

# # paso 3
# for i in range(2):
#     nom = input("Ingresa un miebro nuevo para los beatles: ")
#     beatles.append(nom)
# print("Paso 3:", beatles)

# # paso 4
# del beatles[-1]
# del beatles[-1]
# print("Paso 4:", beatles)

# # paso 5
# beatles.insert(0, "Ringo Starr")
# print("Paso 5:", beatles)

# # probando la longitud de la lista
# print("Los Fav", len(beatles))


# LABORATORIO 3
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unicos = []

for num in my_list:
    if num not in unicos:
        unicos.append(num)

print("La lista con elementos únicos:")
print(unicos)  