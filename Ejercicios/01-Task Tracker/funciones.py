from datetime import datetime
import json

DATOS_JSON = 'datos.json'


#------------GENERALES-------------------
# Leer archivo JSON
def leerArchivo():
    with open(DATOS_JSON, 'r', encoding='utf-8') as archivo:
        tareas = json.load(archivo)
        return tareas


# Guardar archivo JSON
def guardarArchivo(tareas):
    with open(DATOS_JSON, 'w', encoding='utf-8') as f:
        json.dump(tareas, f, ensure_ascii=False, indent=4)


# Convertir fecha
def transFecha(fecha):
    objeto_fecha = datetime.fromisoformat(fecha)
    return objeto_fecha.strftime("%d/%m/%Y %H:%M")


#------------ESPECIFICOS-------------------
# Crear tarea
def crear(descripcion):
    # 1. Cargar los datos existentes o crear una lista vacía si el archivo no existe
    try:
        tareas = leerArchivo()
    except (FileNotFoundError, json.JSONDecodeError):
        tareas = []
    
    # 2. Crear la nueva tarea
    nueva_tarea = {
        "id": len(tareas) + 1,
        "description": descripcion,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updateAt": datetime.now().isoformat(),
    }
    
    # 3. Agregar la tarea a la lista
    tareas.append(nueva_tarea)
    
    # 4. Guardar la lista actualizada en el archivo JSON
    try:
        guardarArchivo(tareas)
        print(f"Task added successfully (ID: {nueva_tarea['id']})")
        
    except Exception as error:
        print(type(error))
            
            
# Editar tarea
def editar(id, description):
    # 1. Cargar los datos existentes o crear una lista vacía si el archivo no existe
    tareas = leerArchivo()
    
    # 2. Modificar la descripcion de la tarea con el id dado
    encontrado = False
    for tarea in tareas:
        if tarea.get('id') == int(id):
            tarea['description'] = description
            encontrado = True
            break
    
    if not encontrado:
        print(f"No se encontró ninguna tarea con el ID: {id}")
        return
    
    # 3. Guardar los cambios
    try:
        guardarArchivo(tareas)
        print(f"Task modified successfully (ID: {'id'})")
    except Exception as error:
        print(type(error))
        

# Eliminar tarea
def eliminar(id):
    # 1. Cargar los datos existentes
    tareas = leerArchivo()
    
    # 2. Buscar si existe 
    encontrado = False
    for tarea in tareas:
        if tarea.get('id') == id:
            encontrado = True
            break

    # 3. Filtrar la lista excluyendo el elemento con el id indicado
    if encontrado:
        tareas = [item for item in tareas if item.get("id") != id]
        
        # 4. Guardar los cambios
        try:
            guardarArchivo(tareas)
            print(f"Task delete successfully (ID: {id})")
        except Exception as error:
            print(type(error))
    else:
        print('El id no existe')

   
# Cambiar status
def setStatus(id, status):
    # 1. Cargar los datos existentes 
    tareas = leerArchivo()

    # Modificar el elemento deseado
    encontrado = False
    for tarea in tareas:
        if(tarea['id'] == id):
            tarea['status'] = status
            encontrado = True
    
    if not encontrado:
        print(f"No se encontró ninguna tarea con el ID: {id}")
        return
    
    # 3. Guardar los cambios
    try:
        guardarArchivo(tareas)
        print(f"Task status modified successfully (ID: {'id'})")
    except Exception as error:
        print(type(error))        


# Listar tareas
def listar(estado = all):
    # 1. Cargar los datos existentes 
    try:
        with open(DATOS_JSON, 'r', encoding='utf-8') as archivo:
            # 1. Cargar los datos existentes
            tareas = leerArchivo()
            
            # 2. Verificar que tenga tareas
            if(len(tareas) == 0):
                print('No existe ninguna tarea aun')
            
            # 2. Imprimir las tareas 
            for task in tareas:
                if(estado == all):
                    print(f"{task['id']} - {task['description']} - {task['status']} - {transFecha(task['createdAt'])} - {transFecha(task['updateAt'])}")
                elif(task['status'] == estado):
                    print(f"{task['id']} - {task['description']} - {task['status']} - {transFecha(task['createdAt'])} - {transFecha(task['updateAt'])}")
    except FileNotFoundError:
        print("El archivo no existe.")
    except json.JSONDecodeError:
        print(f"El archivo no tiene un formato JSON válido.") 
    
  
    
    
        
        
