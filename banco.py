from Datos import*

def Datos_tarjeta():
    while True:
        try:
            cargar_datos(Ruta_JSON_Banco, Banco)
            numero_tarjeta = input("Ingrese el numero de tarjeta:  ")
            if Banco.get(numero_tarjeta,None) == None:
                Banco[numero_tarjeta]={}
                print("""
                        1. Visa
                        2. Master
                        3. American
                        4. salir
                        """)
                tipo_tarjeta = input("Ingrese la opcion deseada:  ")
                info_tarjeta = {}
                info_tarjeta["Tipo de tarjeta"] = tipo_tarjeta
                info_tarjeta["mes"] = input("Mes de Validez:  ")
                info_tarjeta["ano"] = input("Ano de Validez:  ")
                info_tarjeta["COD verificacion"] = input("COD Verificacion:  ")
                Banco[numero_tarjeta] = info_tarjeta
                codigo_Cleinte = input("Codigo de cleinte:  ")
                Banco[numero_tarjeta]["Codigo de cleinte"] = {}
                Banco[numero_tarjeta]["Codigo de cleinte"][codigo_Cleinte]={}
                guardar_datos(Ruta_JSON_Banco, Banco)
                break
            else:
                print("Numero de tarjeta ya Registrado")
        except Exception as e:
            print(f"El error fue causado por {e}")
            continue
            



def Datos_usuario():
    while True:
        try:
            cargar_datos(Ruta_JSON_Banco, Banco)
            numero_tarjeta = input("Ingrese el numero de tarjeta:  ")
            codigo_Cleinte = input("Codigo de cleinte:  ")
            info_Cliente = {}
            info_Cliente["Nombre del cliente"] =input("Nombre de cleinte:  ")   
            info_Cliente["Cedula de Ciudadanía"] =input("Cedula de Ciudadanía:  ")
            info_Cliente["Número de teléfono de contacto"] =input("Número de teléfono de contacto:  ")
            info_Cliente["Sexo"] =input("Sexo:  ")
            if numero_tarjeta in Banco:
                Banco[numero_tarjeta]["Codigo de cleinte"][codigo_Cleinte]=info_Cliente
                guardar_datos(Ruta_JSON_Banco, Banco)
                return
            else:
                print("Numero de tarjeta no Registrado")
        except Exception as e:
            print(f"El error fue causado por {e}")
            continue
        

                
def impresion_1 ():
    cargar_datos(Ruta_JSON_Banco, Banco)
    for llave_1, valor_1 in Banco.items():
        Cod = valor_1.get("Codigo de cleinte",{})
        for llave, valor in Cod.items():
            print()
            print(f"""
                Numero de tarjeta:  {llave_1}
                Nombre cliente: {valor.get("Nombre del cliente", "No registra")}
                Documento cliente: {valor.get("Cedula de Ciudadanía", "No registra")}
                Tipo de Tarjeta: {valor_1.get("Tipo de tarjeta",None)}
                mes: {valor_1.get("mes",None)}
                ano: {valor_1.get("ano",None)}
                COD verificacion: {valor_1.get("COD verificacion",None)}
                Codigo de cleinte: {llave}
                """)
            print()
            



def impresion_2 ():
    cargar_datos(Ruta_JSON_Banco, Banco)
    while True:
        try:
            numero_tarjeta = input("Ingrese el numero de tarjeta:  ")
            if numero_tarjeta in Banco:
                
                print(f"""  
                    Numero detarjeta: {numero_tarjeta}
                        Tipo de Tarjeta: {Banco[numero_tarjeta]["Tipo de tarjeta"]}
                        mes: {Banco[numero_tarjeta]["mes"]}
                        ano: {Banco[numero_tarjeta]["Tipo de tarjeta"]}
                        COD verificacion: {Banco[numero_tarjeta]["COD verificacion"]}
                    """)
                info = Banco[numero_tarjeta]["Codigo de cleinte"]
                for llave, valor in info.items():
                    print(f"""   
                        Codigo cleinte {llave}
                        Nombre cliente: {valor.get("Nombre del cliente", "No registra")}
                        Documento cliente: {valor.get("Cedula de Ciudadanía", "No registra")}
                        Número de teléfono de contacto: {valor.get("Número de teléfono de contacto", "No registra")}
                        Sexo: {valor.get("Sexo", "No registra")}
                        """)
                return
            else:
                print("Numero de tarjeta no Registrado")
        except Exception as e:
            print(f"Ingrese bien el Numero de documento {e}")
            continue
        
def impresion_3():
    cont_visa=0
    cont_master=0
    cargar_datos(Ruta_JSON_Banco, Banco)
    for llave_1, valor_1 in Banco.items():
        if valor_1.get("Tipo de tarjeta",{}) =="Visa":
            cont_visa = cont_visa + 1
        if valor_1.get("Tipo de tarjeta",{}) =="Master":
            cont_master = cont_master + 1
    print(cont_visa)
    print(cont_master)
    return
            

            

    
    
def Datos_Modificar():
    while True:
        try:
            cargar_datos(Ruta_JSON_Banco, Banco)
            numero_tarjeta = input("Ingrese el numero de tarjeta:  ")
            if Banco.get(numero_tarjeta,None) != None:
                Banco[numero_tarjeta]["Tipo de tarjeta"]= input("Tipo:  ")
                Banco[numero_tarjeta]["mes"]= input("mes:  ")
                Banco[numero_tarjeta]["ano"]= input("ano:  ")
                Banco[numero_tarjeta]["COD verificacion"]= input("COD verificacion:  ")
                guardar_datos(Ruta_JSON_Banco, Banco)
                break
            else:
                print("Numero de tarjeta ya Registrado")
        except Exception as e:
            print(f"El error fue causado por {e}")
            continue


Datos_tarjeta()