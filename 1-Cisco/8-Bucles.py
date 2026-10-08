# WHILE
# contador = 10
# while contador:
#     print("El numero es:", contador)
#     contador -= 1

# FOR
# for i in range(2, 20, 2):
#     print("El numero es:", i)


# BREAK
# for i in range(2, 20, 2):
#     print("El numero es:", i)
#     if i == 12: break


# CONTINUE
# for i in range(2, 20, 2):
#     if i == 12: continue
#     print("El numero es:", i)


# FOR-ELSE
# for i in range(2, 20, 2):
#     if i == 12: continue
#     print("El numero es:", i)
# else:
#     print("Fin")


# LABORATORIO 1
# La forma en que lo hemos utilizado aquí se llama impresión multilínea. 
# Puedes utilizar comillas triples para imprimir cadenas en varias líneas para facilitar la lectura del texto o crear un diseño especial basado en texto.
# secret_number = 777

# print(
# """
# +================================+
# | ¡Bienvenido a mi juego, muggle!|
# | Introduce un número entero     |
# | y adivina qué número he        |
# | elegido para ti.               |
# |¿Cuál es el número secreto?     |
# +================================+
# """)

# while True:
#     num = int(input("Ingresa un numero entero: "))
    
#     if num == secret_number:
#         print("¡Bien hecho, muggle! Eres libre ahora.")
#         break
#     else:
#         print("¡Ja, ja! ¡Estás atrapado en mi bucle!")


# LABORATORIO 2
# import time
# # Escribe un bucle for que cuente hasta cinco.
#     # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
#     # Cuerpo del bucle, emplea : time.sleep(1)
# for i in range(1, 6):
#     print(i,"Mississippi")
#     time.sleep(1)

# # Escribe una función print con el mensaje final.
# print("¡Listos o no, ahí voy!")


# LABORATORIO 3
# while True:
#     word = input("Ingresa una palabra: ")
#     if word == "chupacabra":
#         break
# print("Has dejado el bucle con éxito.")


# LABORATORIO 4
# user_word = input("Ingresa una palabra: ")

# user_word = user_word.upper()

# for letter in range(len(user_word)):
#     if user_word[letter] == "A":
#         continue
#     elif user_word[letter] == "E":
#         continue
#     elif user_word[letter] == "I":
#         continue
#     elif user_word[letter] == "O":
#         continue
#     elif user_word[letter] == "U":
#         continue
    
#     print(user_word[letter])
    

# LABORATORIO 5
# user_word = input("Ingresa una palabra: ")
# user_word = user_word.upper()
# word_without_vowels = ""

# for letter in range(len(user_word)):
#     if user_word[letter] == "A":
#         word_without_vowels += user_word[letter]
#         continue
#     elif user_word[letter] == "E":
#         word_without_vowels += user_word[letter]
#         continue
#     elif user_word[letter] == "I":
#         word_without_vowels += user_word[letter]
#         continue
#     elif user_word[letter] == "O":
#         word_without_vowels += user_word[letter]
#         continue
#     elif user_word[letter] == "U":
#         word_without_vowels += user_word[letter]
#         continue
    
#     print(user_word[letter])
# print(word_without_vowels)
    
    
# LABORATORIO 6
# blocks = int(input("Ingresa el número de bloques: "))

# height = 0
# block_necesario = 1

# while blocks >= block_necesario:
#     blocks -= block_necesario
#     height += 1
#     block_necesario += 1

# print("La altura de la pirámide:", height)
# print("Bloques sobrantes:", blocks)


# LABORATORIO 7
# Pedir un número natural al usuario
c0 = int(input("Ingresa un número natural (mayor que 0): "))

# Verificar que el número sea válido (mayor que 0)
if c0 <= 0:
    print("El número debe ser entero positivo (no negativo y no cero).")
else:
    pasos = 0  # Contador de pasos
    
    # Bucle mientras c0 sea diferente de 1
    while c0 != 1:
        print(c0)  # Mostrar el valor actual de c0
        
        # Si c0 es par
        if c0 % 2 == 0:
            c0 = c0 // 2
        # Si c0 es impar
        else:
            c0 = 3 * c0 + 1
            
        pasos += 1  # Incrementar el contador de pasos
        
    # Imprimir el 1 final y el total de pasos
    print(1)
    print(f"Total de pasos necesarios: {pasos}")
