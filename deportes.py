from Datos import*


def Crear_dict ():
    while True:
        try:
            cargar_datos(Ruta_JSON_Deportes, Deportes)
            
            print("""
                ********************************
                Inscripcion de participantes
                ********************************
                """)
            
            Carrera = input("""
                    Ingrese el numero para continuar
                            
                    1. Atletismo
                    2. Ciclismo
                    3. Patinaje
                    4. Salir
                    """)
            if Carrera == "1":
                if Deportes.get("Atletismo",None) == None:
                    Deportes["Atletismo"]={}
                    Documento = input("ingrese el Documento:  ")
                    info_deportista = {
                            "Nombre":input("Nombre de participante:  "),
                            "Numero":input("Numero de participante:  "),
                            "Genero":input("Genero de participante:  "),
                            "Posicion":None,
                            "Tiempo":None     
                    }
                    if Deportes["Atletismo"].get(Documento,None) == None:
                        Deportes["Atletismo"][Documento]={}
                        Deportes["Atletismo"][Documento] = info_deportista
                        guardar_datos(Ruta_JSON_Deportes, Deportes)
                        return
                else:
                    Documento = input("ingrese el Documento:  ")
                    info_deportista = {
                            "Nombre":input("Nombre de participante:  "),
                            "Numero":input("Numero de participante:  "),
                            "Genero":input("Genero de participante:  "),
                            "Posicion":None,
                            "Tiempo":None     
                    }
                    if Deportes["Atletismo"].get(Documento,None) == None:
                        Deportes["Atletismo"][Documento]={}
                        Deportes["Atletismo"][Documento] = info_deportista
                        guardar_datos(Ruta_JSON_Deportes, Deportes)
                        return
                    
            if Carrera == "2":
                if Deportes.get("Ciclismo",None) == None:
                    Deportes["Ciclismo"]={}
                    Documento = input("ingrese el Documento:  ")
                    info_deportista = {
                            "Nombre":input("Nombre de participante:  "),
                            "Numero":input("Numero de participante:  "),
                            "Genero":input("Genero de participante:  "),
                            "Posicion":None,
                            "Tiempo":None     
                    }
                    if Deportes["Ciclismo"].get(Documento,None) == None:
                        Deportes["Ciclismo"][Documento]={}
                        Deportes["Ciclismo"][Documento] = info_deportista
                        guardar_datos(Ruta_JSON_Deportes, Deportes)
                        return
                else:
                    Documento = input("ingrese el Documento:  ")
                    info_deportista = {
                            "Nombre":input("Nombre de participante:  "),
                            "Numero":input("Numero de participante:  "),
                            "Genero":input("Genero de participante:  "),
                            "Posicion":None,
                            "Tiempo":None     
                    }
                    if Deportes["Ciclismo"].get(Documento,None) == None:
                        Deportes["Ciclismo"][Documento]={}
                        Deportes["Ciclismo"][Documento] = info_deportista
                        guardar_datos(Ruta_JSON_Deportes, Deportes)
                        return
                    
            if Carrera == "3":
                if Deportes.get("Patinaje",None) == None:
                    Deportes["Patinaje"]={}
                    Documento = input("ingrese el Documento:  ")
                    info_deportista = {
                            "Nombre":input("Nombre de participante:  "),
                            "Numero":input("Numero de participante:  "),
                            "Genero":input("Genero de participante:  "),
                            "Posicion":None,
                            "Tiempo":None     
                    }
                    if Deportes["Patinaje"].get(Documento,None) == None:
                        Deportes["Patinaje"][Documento]={}
                        Deportes["Patinaje"][Documento] = info_deportista
                        guardar_datos(Ruta_JSON_Deportes, Deportes)
                        return
                else:
                    Documento = input("ingrese el Documento:  ")
                    info_deportista = {
                                "Nombre":input("Nombre de participante:  "),
                                "Numero":input("Numero de participante:  "),
                                "Genero":input("Genero de participante:  "),
                                "Posicion":None,
                                "Tiempo":None     
                        }
                    if Deportes["Patinaje"].get(Documento,None) == None:
                            Deportes["Patinaje"][Documento]={}
                            Deportes["Patinaje"][Documento] = info_deportista
                            guardar_datos(Ruta_JSON_Deportes, Deportes)
                            return
                    
            if Carrera == "4":
                
                return
            
            else:
                print("Opcion no Valida")
                continue
        except Exception as e:
            print(f"Error causado por:{e}")
    

def Modificar_info():
    while True:
        try:
            cargar_datos(Ruta_JSON_Deportes, Deportes)
            print("""
                        ********************************
                                Modificar info
                        ********************************
                        """)
                    
            Carrera = input("""
                            Ingrese el numero para continuar  
                            1. Atletismo
                            2. Ciclismo
                            3. Patinaje
                            4. Salir
                            """)
            if Carrera == "1":
                Documento = input("ingrese el Documento:  ")
                Deportes["Atletismo"][Documento]["Nombre"]=input("Nombre a Modificar:   ")
                Deportes["Atletismo"][Documento]["Numero"]=input("Numero a Modificar:   ")
                Deportes["Atletismo"][Documento]["Genero"]=input("Genero a Modificar:   ")
                guardar_datos(Ruta_JSON_Deportes, Deportes)
                return
            if Carrera == "2":
                Documento = input("ingrese el Documento:  ")
                Deportes["Ciclismo"][Documento]["Nombre"]=input("Nombre a Modificar:   ")
                Deportes["Ciclismo"][Documento]["Numero"]=input("Numero a Modificar:   ")
                Deportes["Ciclismo"][Documento]["Genero"]=input("Genero a Modificar:   ")
                guardar_datos(Ruta_JSON_Deportes, Deportes)
                return
            if Carrera == "3":
                Documento = input("ingrese el Documento:  ")
                Deportes["Patinaje"][Documento]["Nombre"]=input("Nombre a Modificar:   ")
                Deportes["Patinaje"][Documento]["Numero"]=input("Numero a Modificar:   ")
                Deportes["Patinaje"][Documento]["Genero"]=input("Genero a Modificar:   ")
                guardar_datos(Ruta_JSON_Deportes, Deportes)
                return
            
            if Carrera == "4":
                return
            else:
                print("Opcion no Valida")
                continue
        except Exception as e:
            print(f"error Causado por {e}")
            
def Agregar_posicion ():
    while True:
        try:
            cargar_datos(Ruta_JSON_Deportes, Deportes)
            print("""
                        ********************************
                            Agregar posicion y Tiempo
                        ********************************
                        """)
                    
            Carrera = input("""
                            Ingrese el numero para continuar  
                            1. Atletismo
                            2. Ciclismo
                            3. Patinaje
                            4. Salir
                            """)
            
            if Carrera == "1":
                Documento = input("ingrese el Documento:  ")
                Deportes["Atletismo"][Documento]["Posicion"]=int(input("Posicion:   "))
                Deportes["Atletismo"][Documento]["Tiempo"]=input("Tiempo:   ")
                guardar_datos(Ruta_JSON_Deportes, Deportes)
                return
            if Carrera == "2":
                Documento = input("ingrese el Documento:  ")
                Deportes["Ciclismo"][Documento]["Posicion"]=int(input("Posicion:   "))
                Deportes["Ciclismo"][Documento]["Tiempo"]=input("Tiempo:   ")
                guardar_datos(Ruta_JSON_Deportes, Deportes)
                return
            if Carrera == "3":
                Documento = input("ingrese el Documento:  ")
                Deportes["Patinaje"][Documento]["Posicion"]=int(input("Posicion:   "))
                Deportes["Patinaje"][Documento]["Tiempo"]=input("Tiempo:   ")
                guardar_datos(Ruta_JSON_Deportes, Deportes)
                return
            if Carrera == "4":
                return
            else:
                print("Opcion no Valida")
                continue
                
        except Exception as e:
            print(f"error Causado por {e}")
            
            

def ver_todos ():
    cargar_datos(Ruta_JSON_Deportes, Deportes)
    for llave, valor in Deportes.items():
        print(f"""
                DEPORTE:  {llave}
                """)
        for llave_2, valor_2 in valor.items():
            print(f"""
                Nombre: {valor_2.get("Nombre")}
                Documento:  { llave_2}
                Posicion: {valor_2.get("Posicion")}
                Tiempo: {valor_2.get("Tiempo")}
                """)
            
    
def ver_ciclismo ():
    cargar_datos(Ruta_JSON_Deportes, Deportes)
    for llave, valor in Deportes.items():
        if llave == "Ciclismo":
            print(f"""
                    DEPORTE:  {llave}
                    """)
            for llave_2, valor_2 in valor.items():
                print(f"""
                    Nombre: {valor_2.get("Nombre")}
                    Documento:  { llave_2}
                    Posicion: {valor_2.get("Posicion")}
                    Tiempo: {valor_2.get("Tiempo")}
                    """)
    
def ver_Atetismo ():
    cargar_datos(Ruta_JSON_Deportes, Deportes)
    for llave, valor in Deportes.items():
        if llave == "Atletismo":
            print(f"""
                    DEPORTE:  {llave}
                    """)
            for llave_2, valor_2 in valor.items():
                print(f"""
                    Nombre: {valor_2.get("Nombre")}
                    Documento:  { llave_2}
                    Posicion: {valor_2.get("Posicion")}
                    Tiempo: {valor_2.get("Tiempo")}
                    """)
                
def ver_Patinaje ():
    cargar_datos(Ruta_JSON_Deportes, Deportes)
    for llave, valor in Deportes.items():
        if llave == "Patinaje":
            print(f"""
                    DEPORTE:  {llave}
                    """)
            for llave_2, valor_2 in valor.items():
                print(f"""
                    Nombre: {valor_2.get("Nombre")}
                    Documento:  { llave_2}
                    Posicion: {valor_2.get("Posicion")}
                    Tiempo: {valor_2.get("Tiempo")}
                    """)

def ver_por_documento ():
    cargar_datos(Ruta_JSON_Deportes, Deportes)
    Documento = input("ingrese el Documento:  ")
    for llave, valor in Deportes.items():
            for llave_2, valor_2 in valor.items():
                if llave_2== Documento:
                    print(f"""
                            DEPORTE:  {llave}
                            """)
                    print(f"""
                    Nombre: {valor_2.get("Nombre")}
                    Documento:  { llave_2}
                    Posicion: {valor_2.get("Posicion")}
                    Tiempo: {valor_2.get("Tiempo")}
                    """)
                

def ver_por_posicion ():
    cargar_datos(Ruta_JSON_Deportes, Deportes)
    for llave, valor in Deportes.items():
        print(f"""
                    DEPORTE:  {llave}
                    """)
        for llave_2, valor_2 in valor.items():
            if valor_2.get("Posicion") == 1:
                print(f"""
                    Nombre: {valor_2.get("Nombre")}
                    Documento:  { llave_2}
                    Posicion: {valor_2.get("Posicion")}
                    Tiempo: {valor_2.get("Tiempo")}
                    """)
            if valor_2.get("Posicion") == 2:
                print(f"""
                    Nombre: {valor_2.get("Nombre")}
                    Documento:  { llave_2}
                    Posicion: {valor_2.get("Posicion")}
                    Tiempo: {valor_2.get("Tiempo")}
                    """)
            if valor_2.get("Posicion") == 3:
                print(f"""
                    Nombre: {valor_2.get("Nombre")}
                    Documento:  { llave_2}
                    Posicion: {valor_2.get("Posicion")}
                    Tiempo: {valor_2.get("Tiempo")}
                    """)
            if valor_2.get("Posicion") == 4:
                print(f"""
                    Nombre: {valor_2.get("Nombre")}
                    Documento:  { llave_2}
                    Posicion: {valor_2.get("Posicion")}
                    Tiempo: {valor_2.get("Tiempo")}
                    """)
            if valor_2.get("Posicion") == 5:
                print(f"""
                    Nombre: {valor_2.get("Nombre")}
                    Documento:  { llave_2}
                    Posicion: {valor_2.get("Posicion")}
                    Tiempo: {valor_2.get("Tiempo")}
                    """)
    
    
    
def menu():
    while True:
        try:
            print("""
                ********************************
                            Menu
                ********************************
                """)
            print("""
                1. Agregar un Participante
                2. Modificar un Participante
                3. Agregar posicion y tiempo
                4. ver listado de Participantes
                5. Participantes en Ciclismo
                6. Participantes en Atletismo
                7. Participantes en Patinaje
                8. Participantes por Documento
                9. Los 5 Primeros
                10. Salir
                """)
            
            menu = input("Ingrese su opcion:  ")
            if menu == "1":
                Crear_dict ()
            elif menu == "2":
                Modificar_info()
            elif menu == "3":
                Agregar_posicion ()
            elif menu == "4":
                ver_todos ()
            elif menu == "5":
                ver_ciclismo ()
            elif menu == "6":
                ver_Atetismo ()
            elif menu == "7":
                ver_Patinaje ()
            elif menu == "8":
                ver_por_documento ()
            elif menu == "9":
                ver_por_posicion ()
            elif menu == "10":
                break
            else:
                print("Opcion no Valida")
                continue
                
        except Exception as e:
            print(f"El error es causado por {e}")
            
    
menu()