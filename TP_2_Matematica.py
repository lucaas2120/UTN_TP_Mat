#Parte 2A – Desarrollo del Programa en Python con DNIs
#----------------------------------------------------------------------------------
def funcionesDNI():
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

    def extranjero(dni):
        #2.A.6.expresiones logicas
        #con esta funcion verificamos si el nro. DNI corresponde a un extranjero residente
        #verificando si esta dentro de cierto rango
        if int(dni) > 90000000:
            return True
        else:
            return False

    def es_palindromo(dni):
        #2.A.6.expresiones logicas
        #con esta funcion verificamos si el nro. DNI es un palíndromo
        #comparandolo con un número con los mismos digitos invertidos
        if str(dni)==dni[::-1]:
            return True
        else:
            return False

    def vacantes(cantidad):
        #2.A.6.expresiones logicas
        #con esta funcion verificamos si el grupo tiene menos de 3 integrantes y 
        #mostrando es afirmativo que tiene vacantes
        if cantidad < 3:
            return "¡Grupo con lugares vacantes!"
        else:
            return ""

    def procesarsDNI(dnis):
        #Procesaremos cada uno de los DNI ingresados en las funciones anteriores.
        #Utilizamos la funcion de condicionesLogicas para determinar si los numeros ingresados pueden ser procesados
        conjuntos = [limpiarDigitos(dni) for dni in dnis]

        #Validación para definir que existan los conjuntos
        
        if not conjuntos:
            print("No se ingresaron DNIs, volviendo al menú principal")
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
            print(f"DNI de extranjero residente: {extranjero(dni)}")    #2.A.6.expresiones logicas
            print(f"DNI es palíndromo: {es_palindromo(dni)}")           #2.A.6.expresiones logicas

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
            print(vacantes(len(conjuntos)))                              #2.A.6.expresiones logicas
        else:
            #En caso de que no haya suficientes conjuntos para operar imprimimos el siguiente mensaje
            print("Se deben ingresar más de un DNI para calcular operaciones entre conjuntos.") 


    dnis = solicitarDNI()
    procesarsDNI(dnis)


#Parte 2B – Desarrollo del Programa en Python con Fechas Nacimiento
#----------------------------------------------------------------------------------
def funcionesAnio():
    #Ingreso de años de nacimiento
    anios = []
    cantidad = int(input("¿Cuántas personas hay en el grupo? "))

    for i in range(cantidad):
        anio = int(input("Ingresá el año de nacimiento de la persona " + str(i + 1) + ": "))
        anios.append(anio)
    #Contar si son pares e impares
    pares = 0
    impares = 0

    for anio in anios:
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Cantidad de años pares:", pares)
    print("Cantidad de años impares:", impares)

    #Verificar si todos nacieron después del 2000
    todos_despues_2000 = True

    for anio in anios:
        if anio <= 2000:
            todos_despues_2000 = False

    if todos_despues_2000:
        print("Grupo Z")

    #Función para saber si un año es bisiesto
    def es_bisiesto(anio):
        if anio % 4 == 0:
            if anio % 100 != 0 or anio % 400 == 0:
                return True
        return False

    #Verificar si hay algún año bisiesto
    hay_bisiesto = False

    for anio in anios:
        if es_bisiesto(anio):
            hay_bisiesto = True

    if hay_bisiesto:
        print("Tenemos un año especial")

    #Calcular edades actuales y producto cartesiano
    anio_actual = 2025
    edades = []

    for anio in anios:
        edad = anio_actual - anio
        edades.append(edad)

    print("Producto cartesiano (año, edad):")
    for anio in anios:
        for edad in edades:
            print((anio, edad))


def menuPrincipal():
    #Menu para definir que calculos deseamos realizar.
     while True:
        print("\n- MENU PRINCIPAL")
        print("Bienvenido, que analisis desea ejecutar?")
        print("1. Analizar DNIs")
        print("2. Analizar Años de nacimiento")
        print("3. Salir")
        
        try:
            opcion = int(input("Ingrese una opción (1-3): "))
            if opcion not in [1, 2, 3]:
                print("Opción invalida. Por favor ingrese un numero entre 1 y 3.")
                continue
        except ValueError:
            print("Entrada invalida. Por favor ingrese un numero.")
            continue
        
        #Según opcion ingresada llamamos la funcion indicada.
        if opcion == 1:
            funcionesDNI()
        
        elif opcion == 2:
            funcionesAnio()

        elif opcion == 3:
            print("Saliendo del programa.")
            break

        continuar = input("Deseas hacer otra cosa? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saliendo del programa.")
            break


#Ejecutamos el menú principal
menuPrincipal()