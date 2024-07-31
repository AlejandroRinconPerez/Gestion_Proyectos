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
            Documento = input("ingrese el Documento:  ")
            if Carrera == "1":
                Deportes["Atletismo"][Documento]["Nombre"]=input("Nombre a Modificar:   ")
                Deportes["Atletismo"][Documento]["Numero"]=input("Numero a Modificar:   ")
                Deportes["Atletismo"][Documento]["Genero"]=input("Genero a Modificar:   ")
                guardar_datos(Ruta_JSON_Deportes, Deportes)
                return
            if Carrera == "2":
                Deportes["Ciclismo"][Documento]["Nombre"]=input("Nombre a Modificar:   ")
                Deportes["Ciclismo"][Documento]["Numero"]=input("Numero a Modificar:   ")
                Deportes["Ciclismo"][Documento]["Genero"]=input("Genero a Modificar:   ")
                guardar_datos(Ruta_JSON_Deportes, Deportes)
                return
            if Carrera == "3":
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
            Documento = input("ingrese el Documento:  ")
            if Carrera == "1":
                Deportes["Atletismo"][Documento]["Posicion"]=int(input("Posicion:   "))
                Deportes["Atletismo"][Documento]["Tiempo"]=input("Tiempo:   ")
                guardar_datos(Ruta_JSON_Deportes, Deportes)
                return
            if Carrera == "2":
                Deportes["Ciclismo"][Documento]["Posicion"]=int(input("Posicion:   "))
                Deportes["Ciclismo"][Documento]["Tiempo"]=input("Tiempo:   ")
                guardar_datos(Ruta_JSON_Deportes, Deportes)
                return
            if Carrera == "3":
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
            
    
    
