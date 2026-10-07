# ELEMENTOS DE UN DICCIONARIO
# Crear diccionario
# diccionario = {"gato":"juan", "perro":"benito", "caballo":"pepito" }
# diccionario_vacio = {}

# # Imprimir
# print(diccionario)
# print(diccionario_vacio)

# # Largo del diccionario
# print(len(diccionario))
# print(len(diccionario_vacio))

# # Acceder al elemento
# print(diccionario["perro"])

# # Acceder a clave inexistente
# print(diccionario["dog"]) # error

# # Saber si elemento existe
# valor = "gatoo" in diccionario
# print(valor)


# EXPRESIONES LARGAS
# Sangria francesa
# diccionario = {
#     "gato": "chat",
#     "perro": "chien",
#     "caballo": "cheval"
# }

# METODOS
# Keys
# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
# for key in dictionary.keys():
#     print(key, "->", dictionary[key])
 
# Items
# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
# for spanish, french in dictionary.items():
#     print(spanish, "->", french)

# Cambiar valor a valor
# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
# dictionary['gato'] = 'minou'
# print(dictionary)

# Ordenar 
# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
# for key in sorted(dictionary.keys()):
#     print(key)
    
# Lista de valores
# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
# for french in dictionary.values():
#     print(french)

# Agregar nueva clave y valor
# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
# dictionary['cisne'] = 'cygne'
# print(dictionary) 

# Eliminar clave y valor
# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
# del dictionary['perro']
# print(dictionary) 

# Eliminar ultimo elemntos
# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
# dictionary.popitem()
# print(dictionary)