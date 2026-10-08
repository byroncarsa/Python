# OPERACIONES CON CADENAS
# Cadenas multilineas
# multiline = '''Línea #1
# Línea #2'''
# print(len(multiline))

# Concatenar
# str1 = 'a'
# str2 = 'b'
# print(str1 + str2) # ab
# print(str2 + str1) # ba

# Replicar
# str1 = 'a'
# str2 = 'b'
# print(5 * 'a') # aaaaa
# print('b' * 4) # bbbb

# Index
# Demonstración del método index() method:
# print("aAbByYzZaA".index("b")) # 2
# print("aAbByYzZaA".index("Z")) # 7
# print("aAbByYzZaA".index("A")) # 1

#List
# Demostración de la función list():
# print(list("abcabc")) # ['a', 'b', 'c', 'a', 'b', 'c']

# Count
# Demostración del método count():
# print("abcabc".count("b")) # 2
# print('abcabc'.count("d")) # 0


# CADENAS COMO SECUENCIAS
# Indexacion
# Indexando cadenas.
# the_string = 'silly walks'
# for ix in range(len(the_string)):
#     print(the_string[ix], end=' ') # s i l l y   w a l k s 
    
# Iteracion
# Iterando a través de una cadena.
# the_string = 'silly walks'
# for character in the_string:
#     print(character, end=' ') # s i l l y   w a l k s 
    
# Rebanadas
# Rebanadas
# alpha = "abdefg"
# print(alpha[1:3]) # bd
# print(alpha[3:]) # efg
# print(alpha[:3]) # abd
# print(alpha[3:-2]) # e
# print(alpha[-3:4]) # e
# print(alpha[::2]) # adf
# print(alpha[1::2]) # beg

# In
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# print("f" in alphabet) # True
# print("F" in alphabet) # False
# print("1" in alphabet) # False
# print("ghi" in alphabet) # True
# print("Xyz" in alphabet) # False

# Not in
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# print("f" not in alphabet) # False
# print("F" not in alphabet) # True
# print("1" not in alphabet) # True
# print("ghi" not in alphabet) # False
# print("Xyz" not in alphabet) # True


# CADENAS EN ACCION
# Sorted
# Demostración de la función sorted():
# first_greek = ['omega', 'alpha', 'pi', 'gamma']
# first_greek_2 = sorted(first_greek)
# print(first_greek) # ['omega', 'alpha', 'pi', 'gamma']
# print(first_greek_2) # ['alpha', 'gamma', 'omega', 'pi']

# Sort
# Demostración del método sort():
# second_greek = ['omega', 'alpha', 'pi', 'gamma']
# print(second_greek) # ['omega', 'alpha', 'pi', 'gamma']
# second_greek.sort()
# print(second_greek) # ['alpha', 'gamma', 'omega', 'pi']


# LABORATORIO 1
# digits = [ '1111110',  	# 0
# 	   '0110000',	# 1
# 	   '1101101',	# 2
# 	   '1111001',	# 3
# 	   '0110011',	# 4
# 	   '1011011',	# 5
# 	   '1011111',	# 6
# 	   '1110000',	# 7
# 	   '1111111',	# 8
# 	   '1111011',	# 9
# 	   ]

# def print_number(num):
# 	global digits
# 	digs = str(num)
# 	lines = [ '' for lin in range(5) ]
# 	for d in digs:
# 		segs = [ [' ',' ',' '] for lin in range(5) ]
# 		ptrn = digits[ord(d) - ord('0')]
# 		if ptrn[0] == '1':
# 			segs[0][0] = segs[0][1] = segs[0][2] = '#'
# 		if ptrn[1] == '1':
# 			segs[0][2] = segs[1][2] = segs[2][2] = '#'
# 		if ptrn[2] == '1':
# 			segs[2][2] = segs[3][2] = segs[4][2] = '#'
# 		if ptrn[3] == '1':
# 			segs[4][0] = segs[4][1] = segs[4][2] = '#'
# 		if ptrn[4] == '1':
# 			segs[2][0] = segs[3][0] = segs[4][0] = '#'
# 		if ptrn[5] == '1':
# 			segs[0][0] = segs[1][0] = segs[2][0] = '#'
# 		if ptrn[6] == '1':
# 			segs[2][0] = segs[2][1] = segs[2][2] = '#'
# 		for lin in range(5):
# 			lines[lin] += ''.join(segs[lin]) + ' '
# 	for lin in lines:
# 		print(lin)


# print_number(int(input("Ingresa el número que deseas mostrar: ")))

# LABORATORIO 2
# Ingresa el texto a encriptar.
# text = input("Ingresa un mensaje: ")

# # Ingresar un valor de cambio válido (repitelo hasta que tengas éxito).
# shift = 0

# while shift == 0:
#     try:    
#         shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
#         if shift not in range(1,26):
#         	raise ValueError
#     except ValueError:
#         shift = 0
#     if shift == 0:
#         print("¡Valor de cambio inválido!")

# cipher = ''

# for char in text:
#     # ¿Es un letra?
#     if char.isalpha():
#         # Cambia su código.
#         code = ord(char) + shift
#         # Encontrar el código de la primera letra (mayúscula o minúscula).
#         if char.isupper():
#             first = ord('A')
#         else:
#             first = ord('a')
#         # Realizar corrección.
#         code -= first
#         code %= 26
#         # Agregar carácter codificado al mensaje.
#         cipher += chr(first + code)
#     else:
#         # Agregar carácter original al mensaje.
#         cipher += char

# print(cipher)

# LABORATORIO 3
# text = input("Ingresa un texto: ")

# # Quitar todos los espacios...
# text = text.replace(' ','')

# # ... y revisar si la palabra es igual en ambos sentidos
# if len(text) > 1 and text.upper() == text[::-1].upper():
# 	print("Es un palíndromo")
# else:
# 	print("No es un palíndromo")
 
# LABORATORIO 4
# str_1 = input("Ingresa la primera cadena: ")
# str_2 = input("Ingresa la segunda cadena: ")

# strx_1 = ''.join(sorted(list(str_1.upper().replace(' ',''))))
# strx_2 = ''.join(sorted(list(str_2.upper().replace(' ',''))))
# if len(strx_1) > 0 and strx_1 == strx_2:
# 	print("Anagramas")
# else:
# 	print("No son anagramas")
 
# LABORATORIO 5
# date = input("Ingresa tu fecha de cumpleaños (en el siguiente formato: AAAAMMDD o AAAADDMM, 8 dígitos): ")
# if len(date) != 8 or not date.isdigit():
#     print("Formato de fecha inválida.")
# else:
#     while len(date) > 1:
#         the_sum = 0
#         for dig in date:
#             the_sum += int(dig)
#         print(date)
#         date = str(the_sum)
#     print("Tu Dígito de la Vida es: " + date)
	
# LABORATORIO 6
# word = input("Ingresa la palabra que deseas encontrar: ").upper()
# strn = input("Ingresa la cadena en donde deseas buscar: ").upper()

# found = True
# start = 0

# for ch in word:
# 	pos = strn.find(ch, start) 
# 	if pos < 0:
# 		found = False
# 		break
# 	start = pos + 1
# if found:
# 	print("Si")
# else:
# 	print("No")

# LABORATORIO 7
# Una función que verifica si una lista pasada como argumento contiene
# nueve dígitos del '1' al '9'.
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# Una lista de filas que representan el Sudoku.
rows = [ ]
for r in range(9):
    ok = False
    while not ok:
        row = input("Ingresa fila #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Datos de fila incorrectos: se requieren 9 dígitos")
    rows.append(row)

ok = True

# Comprobar si todas las filas son correctas.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Comprobar si todas las columnas son correctas.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Comprobar si todos los subcuadrados (3x3) son correctos.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Hacer una cadena que contenga todos los dígitos de un subcuadrado.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Imprimir el veredicto final.
if ok:
    print("Si")
else:
    print("No")


