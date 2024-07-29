from Datos import*

def anadir_proyecto():
    while True:
        try:
            cargar_datos(Ruta_JSON_Proyectos, Proyectos)
            codigo_proyecto = input('Codigo de Proyecto:  ')
            if Proyectos.get(codigo_proyecto, None) == None:
                Proyectos[codigo_proyecto]={}
                info_proyectos = {}
                info_proyectos["Nombre"] = input('Ingrese el Nombre:  ')
                info_proyectos["Fecha_incio"] = input('Ingrese el Fecha de Inicio:   ')
                info_proyectos["Fecha_fin"] = input('Ingrese el Fecha dfe FIN:   ')
                info_proyectos["Tareas"] = {}
                Proyectos[codigo_proyecto]=info_proyectos
                guardar_datos(Ruta_JSON_Proyectos, Proyectos)
                return
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            continue
        
def Tareas_Nuevas ():
    while True:
        try:
            cargar_datos(Ruta_JSON_Proyectos, Proyectos)
            codigo_proyecto = input('Codigo de Proyecto:  ')
            if Proyectos.get(codigo_proyecto, None) == None:
                print("Proyecto No Registrado")
                return
            codigo_Tarea = input("codigo de tareas")
            if codigo_Tarea == "salir":
                break
            if  Proyectos[codigo_proyecto]["Tareas"].get(codigo_Tarea,None) == None:
                info_Tareas = {}
                info_Tareas["Nombre"] = input('Ingrese el Nombre:  ')
                info_Tareas["descripcion"] = input('Ingrese el Fecha de Inicio:   ')
                info_Tareas["fecha_vencimiento"] = input('Ingrese el Fecha dfe FIN:   ')
                info_Tareas["estado"] = input('Ingrese el Fecha dfe FIN:   ')
                Proyectos[codigo_proyecto]["Tareas"][codigo_Tarea]={}
                Proyectos[codigo_proyecto]["Tareas"][codigo_Tarea]=info_Tareas
                guardar_datos(Ruta_JSON_Proyectos, Proyectos)

            else:
                print("Codigo ya Registrado")
                continue
                
        except Exception as e:
            print(f"Error al cargar Datos {e}")
            continue
            
            
            
            
                
def ver_Proyectos():
    while True:
        try:
            cargar_datos(Ruta_JSON_Proyectos, Proyectos)
            for proyecto, datos in Proyectos.items():
                tareas = datos.get("Tareas",{})
                if tareas:
                        print("Tareas:")
                        for tarea_id, tarea in tareas.items():
                            print(f"  ID: {tarea_id}")
                            print(f"    Nombre: {tarea.get('Nombre', 'Sin nombre')}")
                            print(f"    Descripción: {tarea.get('descripcion', 'Sin descripción')}")
                            print(f"    Fecha de vencimiento: {tarea.get('fecha_vencimiento', 'Sin fecha')}")
                            print(f"    Estado: {tarea.get('estado', 'Sin estado')}")
                            print()  # Línea en blanco para separar tareas
                else:
                    print("No Found")
            return
                    
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            continue
                
def ver_Proyectos_2 ():
      while True:
        try:
            cargar_datos(Ruta_JSON_Proyectos, Proyectos)
            for proyecto, datos in Proyectos.items():
                Tareas = datos.get("Tareas", {})
                if Tareas:
                    print("Tareas")
                    for ids , datos_t in Tareas.items():
                        print(f"ID:  {ids}")
                        print(f"Nombre: {datos_t.get("Nombre")}")
                        
                
            return
                    
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            continue
        
def more ():
    while True:
        try:
            cargar_datos(Ruta_JSON_Proyectos, Proyectos)
            for llave, valor in Proyectos.items():
                print(f"Nombre: {valor.get("Nombre")}")
                print(f"Fecha_incio: {valor.get("Fecha_incio")}")
                print(f"Fecha_fin: {valor.get("Fecha_fin")}")
                print()
                Tareas = valor.get("Tareas",{})
                print()
                if Tareas:
                    print("Tareas")
                    for llave, valor in Tareas.items():
                        print(f"ID:  {llave}")
                        print(f"estado {valor.get("estado")}")
                        print()
            return
                
        except Exception as e:
            print(f"El error es {e}")
            
def delete():
    cargar_datos(Ruta_JSON_Proyectos, Proyectos)
    codigo_proyecto = input('Codigo de Proyecto:  ')
    if Proyectos.get(codigo_proyecto, None) == None:
        print("Proyecto No Registrado")
        return
    Tarea_delete = input('Tarea:  ')
    if Proyectos[codigo_proyecto]["Tareas"].get(Tarea_delete):
        Proyectos[codigo_proyecto]["Tareas"].pop(Tarea_delete)
        guardar_datos(Ruta_JSON_Proyectos, Proyectos)
    else:
        print('Tarea no existe')
        
        
            
delete()
    
    
