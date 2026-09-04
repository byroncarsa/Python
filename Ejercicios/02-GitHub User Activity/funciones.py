import requests

def convertirEvento(evento):
    if(evento == 'CreateEvent'):
        return 'Create'
    elif(evento == 'PushEvent'):
        return 'Push'
        
    
def obtener_actividad(usuario):
    # Endpoint de la API de GitHub para eventos públicos del usuario
    url = f"https://api.github.com/users/{usuario}/events"
    
    # Es buena práctica incluir un User-Agent
    headers = {"Accept": "application/vnd.github+json"}
    
    try:
        response = requests.get(url, headers=headers)
        
        # Si la petición es correcta (Código 200)
        if response.status_code == 200:
            eventos = response.json()
            
            if eventos:
                print(f"--- Últimos 5 eventos de {usuario} ---")
                # Mostramos los 5 eventos más recientes
                for evento in eventos[:5]:
                    tipo = convertirEvento(evento.get("type"))
                    repo = evento.get("repo", {}).get("name")
                    print(f"- {tipo} {repo}")
        else:
            print("El usuario no existe")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None





        