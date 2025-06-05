def solicitarDNI():
    #Solicitamos el ingreso del DNI, para finalizar ingrese una F, equivalente a FIN
    dnis = []
    #Hacemos un loop para que ingrese su dni de a uno, utilizamos .strip() para eliminar espacios en blanco
    while True: 
        dni = input("Por favor, ingrese un DNI (Para finalizar ingrese F)\n").strip()
        if dni.upper() == "F":
            break
        #Verificamos que haya ingresado un numero y sea mayor a 6 digitos
        elif dni.isdigit() and len(dni) >= 6:
            dnis.append(dni) #Agregamos a la lista dnis el dni ingresado.
        else:
            print("Dato no válido, debe ingresar un número de al menos 6 cifras")
    return dnis

def limpiarDigitos(dni):
        #Generamos un conjunto de digitos unicos de cada DNI.
    return set(dni)

def frecuenciaDeDigitos(dni):
    #Creamos la frecuencia de cada digito en un DNI.
    frecuencia = {}
    #Recorremos todo el dni, digito por digito e incrementamos en cada ocurrencia. 
    for digito in dni:
        frecuencia[digito] = frecuencia.get(digito, 0) + 1 
    return frecuencia

def sumaDigitos(dni):
    #Sumamos todos los digitos de un DNI.
    total = sum(int(digito) for digito in dni)
    return total

def condicionesLogicas(dnis):
    #Comparaciones entre cada DNI
    #Validamos que la lista no este vacía
    if not dnis:
        return {"existeLista": False}
    
    #Utilizamos la funcion limpiar digitos para tener digitos unicos y tener un array con los conjuntos numericos que se ingresaron
    conjuntos = [limpiarDigitos(dni) for dni in dnis] 
    #Utilizamos el metodo que provee SET llamado "Intersection", el cuál nos dara la interseccion de los conjuntos
    interseccion = set.intersection(*conjuntos)

    #Retornamos el "ExisteLista", en caso de que haya una interseccion y tambien la interseccion que hubo.
    return { "existeLista": len(interseccion)>0,
            "interseccion": interseccion}

def diversidadDigitos(dni):
     #Limpiamos los digitos para que sean unicos en el conjunto
     digitos = limpiarDigitos(dni)
     #Si existen mas de 4 números distintos en el conjunto, lo tomaremos como diversidad alta
     diversidadAlta = len(digitos)> 4
     return {"diversidad_Alta": diversidadAlta}

def procesarsDNI(dnis):
    #Procesaremos cada uno de los DNI ingresados en las funciones anteriores.
    #Utilizamos la funcion de condicionesLogicas para determinar si los numeros ingresados pueden ser procesados
    existeLista = condicionesLogicas(dnis)
    #Hacemos un loop sobre todos los DNIs ingresados imprimiendo los resultados
    for dni in dnis:
        print(f"_____________________")
        print(f"Procesamos DNI:{dni}")
        conjunto = limpiarDigitos(dni)
        print(f"Conjunto: {conjunto}")
        print(f"Frecuencia de dígitos: {frecuenciaDeDigitos(dni)}")
        print(f"Suma de los dígitos: {sumaDigitos(dni)}")
        diversidadAlta = diversidadDigitos(dni)
        print(f"Diversidad alta: {diversidadAlta["diversidad_Alta"]}")
        print(f"_____________________")
    #Si existe una lista con datos válidos
    if existeLista["existeLista"]:

        interseccion = sorted(existeLista["interseccion"])
        print(f"Interseccion entre todos los DNIs: {interseccion}")
    else:
        print("No hay digitos comunes entre los DNIs ingresados.")

dnis = solicitarDNI()
procesarsDNI(dnis)

