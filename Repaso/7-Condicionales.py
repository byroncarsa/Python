# OPERADORES

# print(1 == 2) # Igualdad
# print(1 != 2) # Desigualdad
# print(1 > 2) # Mayor que
# print(1 >= 2) # Mayor igual que
# print(1 < 2) # Menor que
# print(1 <= 2) # Menor igual que


# CONDICIONALES

# if
# contador = 13
# if contador > 10:
#     print("El contador es mayor a 10")
    
# if-else
# contador = 9
# if contador > 10:
#     print("El contador es mayor a 10")
# else:
#     print("El contador en menor o igual a 10")

# if-else anidados
# contador = 12
# if contador > 10:
#     if(contador > 15):
#         print("El contador es mayor a 15")
#     else:
#         print("El contador es menor o igual a 15 pero mayor de 10")
# else:
#     print("El contador en menor o igual a 10")
    
# elif
# contador = 12
# if contador > 10:
#     print("Es mayor a 10")
# elif(contador > 15):
#     print("El contador es mayor a 15")
# else:
#     print("El contador en menor o igual a 10")


#TRUCOS

# Encontrar el numero mas alto
numero1 = int(input("Numero Nª1: "))
numero2 = int(input("Numero Nª2: "))

if numero1 > numero2: numero_alto = numero1
else : numero_alto = numero2

print("El numero mas alto es:", numero_alto)