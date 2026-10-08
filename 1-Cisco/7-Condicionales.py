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
# numero1 = int(input("Numero Nª1: "))
# numero2 = int(input("Numero Nª2: "))

# if numero1 > numero2: numero_alto = numero1
# else : numero_alto = numero2

# print("El numero mas alto es:", numero_alto)


# LABORATORIO 1
# n = int(input("Ingresa un número: "))
# print(n >= 100)


# LABORATORIO 2
# name = input("Introduce el nombre de la flor: ")

# if name == "ESPATIFILIO":
#     print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
# elif name == "espatifilo":
#     print("No, ¡quiero un gran ESPATIFILIO!")
# else:
#     print("¡ESPATIFILIO!, ¡No", name + "!")


# LABORATORIO 3
# income = float(input("Introduce el ingreso anual: "))

# if income < 85528:
# 	tax = income * 0.18 - 556.02
# else:
# 	tax = (income - 85528) * 0.32 + 14839.02

# if tax < 0.0:
# 	tax = 0.0

# tax = round(tax, 0)
# print("El impuesto es:", tax, "pesos")


# LABORATORIO 4
year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")
        
