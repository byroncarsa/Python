import funciones as f
    
while True:
    opcion = input('task-cli ') 
    
    if opcion.split()[0] == 'add':
        try:
            descripcion = opcion.split('"')[1] 
            f.crear(descripcion)
            break
        except IndexError:
            print("Debes agregar una descripcion valida")
        except Exception as error:
            print(type(error))
    
    elif opcion.split()[0] == 'update':
        try:
            id = opcion.split()[1] 
            descripcion = opcion.split('"')[1] 
            f.editar(id, descripcion)
            break
        except IndexError:
            print("Debes agregar una descripcion valida")
        except ValueError:
            print("Debes ingresar una id valida")
        except FileNotFoundError:
            print("El archivo no existe")
        except Exception as error:
            print(type(error))
    
    elif opcion.split()[0] == 'delete':
        try:
            id = int(opcion.split()[1])
            f.eliminar(id)
            break
        except IndexError:
            print("Debes ingresar un id")
        except ValueError:
            print("Debes ingresar un id valida")
        except FileNotFoundError:
            print("El archivo no existe")
        except Exception as error:
            print(type(error))      
                
     
    elif opcion.split()[0] == 'mark-in-progress':
        try:
            id = int(opcion.split()[1])
            f.setStatus(id, 'in-progress')
            break
        except IndexError:
            print("Debes ingresar un id")
        except ValueError:
            print("Debes ingresar un id valida")
        except FileNotFoundError:
            print("El archivo no existe")
        except Exception as error:
            print(type(error))  
    
    
    elif opcion.split()[0] == 'mark-done':
        try:
            id = int(opcion.split()[1])
            f.setStatus(id, 'done')
            break
        except IndexError:
            print("Debes ingresar un id")
        except ValueError:
            print("Debes ingresar un id valida")
        except FileNotFoundError:
            print("El archivo no existe")
        except Exception as error:
            print(type(error))  
    
    
    elif opcion == 'list':
        f.listar()
        break
    
    
    elif opcion == 'list done':
        f.listar('done')
        break
    
    
    elif opcion == 'list todo':
        f.listar('todo')
        break
    
    
    elif opcion == 'list in-progress':
        f.listar('in-progress')
        break
   
           
           
                