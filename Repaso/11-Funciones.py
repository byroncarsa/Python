# DEFINIR FUNCION
# def mensaje(): # Definiendo funciones
#     print("Hola mundo")

# mensaje() # Llamando funcion


# FUNCIONES PARAMETRIZADAS
# def mensaje(num):
#     print("Ingresaste el numero:",num)
    
# mensaje(5)


# TIPOS DE PARAMETROS

# Parametros posicionales
# def mensaje(nombre, apellido):
#     print("Hola", nombre, apellido)

# mensaje("byron", "carsa")

# Palabra clave
# def mensaje(nombre, apellido):
#     print("Hola", nombre, apellido)

# mensaje(apellido = "carsa", nombre = "byron")

# Posicionales y palabra clave
# def mensaje(nombre, apellido, segundo_apellido):
#     print("Hola", nombre, apellido, segundo_apellido)

# mensaje("Byron", segundo_apellido = "sepulveda", apellido = "carsa")

# Valor predeterminado
# def mensaje(nombre, apellido, segundo_apellido = "sepulveda"):
#     print("Hola", nombre, apellido, segundo_apellido)

# mensaje("Byron", apellido = "carsa")


# USO DE RETURN (PARS QUE LAS FUNCIONAES DEVUELVE UN VALOR)

# Sin expresion 
# def feliz_año_nuevo(deseos = True):
#     print("Tres...")
#     print("Dos...")
#     print("Uno...")
    
#     if not deseos:
#         return
    
#     print("Feliz año nuevo")
    
# feliz_año_nuevo(False)

# Con expresion (termina el programa inmediatamente)
# def feliz_año_nuevo():
#     print("Tres...")
#     print("Dos...")
#     print("Uno...")
    
#     return "Feliz año nuevo"
    
# tmp = feliz_año_nuevo()
# print(tmp)


# USO DE NONE
# valor = None

# if valor is None:
#     print("No tienes nigun valor")


# LISTAS Y FUNCIONES

# Para metrizando una lista
# lista = [1, 2, 3]

# def sumar(lista):
#     sum = 0
#     for i in lista:
#         sum += i
#     return sum

# print(sumar(lista))

# Retornando una lista
# def crear_lista(rango):
#     lista = []
#     for i in range(rango):
#         lista.append(i)
#     return lista

# print(crear_lista(5))


# FUNCIONES Y ALCANCE
# def dinero(): # global hace que la variable sea accesible tnto dentro como afuera
#     global valor
#     valor = 100
#     print("El valor es", 100)

# dinero()
# print(valor)


# INTERACION CON LOS ARGUMENTOS

# Variables (modificar la variable dentor no cambia la de afuera)
# def my_function(n):
#     print("Yo recibí", n)
#     n += 1
#     print("Ahora tengo", n)
# var = 1
# my_function(var) 
# print(var) 

# Listas (si se modifica dentro el parametro si modifica la lista)
# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     del my_list_1[0] # Presta atención a esta línea.
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)
 
# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)
    

# MULTIPLES PARAMETROS
# def ft_and_inch_to_m(ft, inch = 0.0):
#     return ft * 0.3048 + inch * 0.0254
 
# def lb_to_kg(lb):
#     return lb * 0.4535923
 
# def bmi(weight, height):
#     if height < 1.0 or height > 2.5 or \
#     weight < 20 or weight > 200:
#         return None
 
#     return weight / height ** 2
 
# print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))


# RECURSIVIDAD
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(10)) # 55


# LABORATORIO 1
# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# test_data = [1900, 2000, 2016, 1987]
# test_results = [False, True, True, False]
# for i in range(len(test_data)):
#     yr = test_data[i]
#     print(yr,"->",end="")
#     result = is_year_leap(yr)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Fallido")


# LABORATORIO 2
# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year,month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res  = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# test_years = [1900, 2000, 2016, 1987]
# test_months = [ 2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
#     yr = test_years[i]
#     mo = test_months[i]
#     print(yr,mo,"-> ",end="")
#     result = days_in_month(yr, mo)
#     if result == test_results[i]:
#         print("OK")
#     else:
#         print("Fallido")


# LABORATORIO 3
# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True

# def days_in_month(year,month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res  = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res

# def day_of_year(year, month, day):
#     days = 0
#     for m in range(1, month):
#         md = days_in_month(year, m)
#         if md == None:
#             return None
#         days += md
#     md = days_in_month(year, month)
#     if day >= 1 and day <= md:
#         return days + day
#     else:
#         return None

# print(day_of_year(2000, 12, 31))


# LABORATORIO 4
# def is_prime(num):
#     for i in range(2, int(1 + num ** 0.5)):
#         if num % i == 0:
#             return False
#     return True

# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
# print()


# LABORATORIO 5
# 1 milla = 1609.344 metros.
# 1 galón = 3.785411784 litros.

def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    liters = 3.785411784
    return liters / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


