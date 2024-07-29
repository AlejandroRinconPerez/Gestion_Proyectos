import json

Proyectos = {}
Banco = {}

Ruta_JSON_Proyectos = "Proyectos.json"
Ruta_JSON_Banco = "Banco.json"



def guardar_datos(Ruta_JSON, Datos):
    try:
        contenido = json.dumps(Datos, indent=4,  ensure_ascii=False)
        with open(Ruta_JSON, "w", encoding='utf-8') as file:
            file.write(contenido)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def cargar_datos(Ruta_JSON, Datos):
    try:
        with open(Ruta_JSON, mode="r", encoding='utf-8') as archivo:
            Datos.update(json.load(archivo))
    except Exception as e:
        print(f"Error al cargar Datos {e}")
        
        
#-----------------------------------------------------------------------
# while True:
#         try:
#             print("rfgrads")
#         except Exception as e:
#             print(f"Ocurrió un error inesperado: {e}")
#             continue
        
# def ver_Proyectos_2 ():
#       while True:
#         try:
#             cargar_datos(Ruta_JSON_Proyectos, Proyectos)
#             for proyecto, datos in Proyectos.items():
#                 Tareas = datos.get("Tareas", {})
#                 if Tareas:
#                     print("Tareas")
#                     for ids , datos_t in Tareas.items():
#                         print(f"ID:  {ids}")
#                         print(f"Nombre: {datos_t.get("Nombre")}")
                        
                
#             return
                    
#         except Exception as e:
#             print(f"Ocurrió un error inesperado: {e}")
#             continue
        

                    