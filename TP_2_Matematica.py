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

def diversidadDigitos(dni):
     #Limpiamos los digitos para que sean unicos en el conjunto
     digitos = limpiarDigitos(dni)
     #Si existen mas de 4 números distintos en el conjunto, lo tomaremos como diversidad alta
     diversidadAlta = len(digitos)> 4
     return diversidadAlta

def unionConjuntos(conjuntos):
    #Utilizamos el metodo set.union() devuelve un nuevo conjunto que contiene todos los elementos de ambos conjuntos, sin duplicados
    union = set.union(*conjuntos)
    return union

def interseccionConjuntos(conjuntos):
    #Utilizamos set.intersection() devuelve un nuevo conjunto que contiene solo los elementos comunes a ambos conjuntos
    interseccion = set.intersection(*conjuntos)
    return interseccion

def diferenciaSimetricaConjuntos(conjuntos):
    #Copiamos el primer conjunto como base.
    diferenciaSimetrica = conjuntos[0].copy()
    #Recorremos todos los conjuntos
    for conjunto in conjuntos[1:]:
        #Utilizamos el metodo symmetric_difference() de un conjunto devuelve este conjunto resultante
        diferenciaSimetrica = diferenciaSimetrica.symmetric_difference(conjunto)
    return diferenciaSimetrica

def diferenciaConjuntos(conjuntos):
    #Esta funcion devuelve la diferencia entre todos los conjuntos.
    #Copiamos el primer conjunto como base
    diferencia = conjuntos[0].copy()
    for conjunto in conjuntos[1:]:
        #Eliminamos los elementos presentes en los demás conjuntos
        diferencia -= conjunto
    return diferencia


def procesarsDNI(dnis):
    #Procesaremos cada uno de los DNI ingresados en las funciones anteriores.
    #Utilizamos la funcion de condicionesLogicas para determinar si los numeros ingresados pueden ser procesados
    conjuntos = [limpiarDigitos(dni) for dni in dnis]

    #Validación para definir que existan los conjuntos
    if not conjuntos:
        print("No se ingresaron DNIs validos.")
        return
        
    #Hacemos un loop sobre todos los DNIs ingresados imprimiendo los resultados
    for dni in dnis:
        print(f"__________________________________________")
        print(f"Procesamos DNI:{dni}")
        conjunto = limpiarDigitos(dni)
        print(f"Conjunto: {conjunto}")
        print(f"Frecuencia de dígitos: {frecuenciaDeDigitos(dni)}")
        print(f"Suma de los dígitos: {sumaDigitos(dni)}")
        print(f"Diversidad alta: {(diversidadDigitos(dni))}")
     
    print(f"__________________________________________")
    
    #Validamos que haya mas de un conjunto para poder realizar las operaciones entre ellos.
    if len(conjuntos) > 1:       
        #Ordenamos los resultados de menor a mayor usando sorted
        interseccion = sorted(interseccionConjuntos(conjuntos))
        union = sorted(unionConjuntos(conjuntos))
        diferencia = sorted(diferenciaConjuntos(conjuntos))
        diferenciaSimetrica = sorted(diferenciaSimetricaConjuntos(conjuntos))
        #Imprimimos los resultados por pantalla
        print(f"Interseccion: {interseccion}")
        print(f"Union: {union}")
        print(f"Diferencia: {diferencia}")
        print(f"Diferencia simetrica: {diferenciaSimetrica}")
    else:
        #En caso de que no haya suficientes conjuntos para operar imprimimos el siguiente mensaje
        print("Se deben ingresar más de un DNI para calcular operaciones entre conjuntos.") 


dnis = solicitarDNI()
procesarsDNI(dnis)

