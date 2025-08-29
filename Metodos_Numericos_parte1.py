import math
import os
os.system('cls')

def biseccion():
    #Valores iniciales para verificar el punto medio
    #Especificaremos el numero de iteraciones, tolerancia en el calculo y el intervalo a analizar...
    iteraciones = 100 # Por defecto asi de chill :v
    print("\n\tEste intervalo sera fijo por referencia\n\t")
    Xi= float(input("Dame el intervalo inicial de (xi): "))
    Xu= float(input("Dame el intevalo final (xu):"))
    iteraciones = int(input("(Por defecto: 100) Elije el numero de iteraciones: "))

    if iteraciones <= 0:
        print("\n Intenta con valores positivos\n\t")
    elif iteraciones >= 100000:
        iteraciones = 100 # De nada xd
    tolerancia= float(input("Dame la Tolerancia por ejemplo(0.0001): "))
    
    #Calculamos si el Intervalo para f(Xi)⋅f(Xu)< 0, para checar que hay un salto de signo 
    # Y verificar que la funcion pasa por el EJE x, entonces tendria una raiz...

    #En caso de que no, Nos daria un resultado en Y, implicando que no hay tal intercepcion con
    # el eje X, por lo tanto no tendria dicha raiz....
    # Esos valores en ese rango,nos daria un valor negativo y otro positivo, 
    # por lo cual hay un salto en los valores implica que hau una raiz
    if funcion(Xi) * funcion(Xu) >= 0:
        print(f"\n\tf(Xi)={Xi} * f(Xu)={Xu} = {funcion(Xi) * funcion(Xu)} \n\tNO EXISTE TAL RAIZ EN ESE INTERVALO...!\n\t") 
        return

    #Calculo del punto medio entre los 2 intevalos xi y xu
    #Pero tendremos como referencia el Error de aproximacion para saber cuando parar las iteraciones
    #Y no iterar toooodo el intervalo, y eso lo hacemos con abs(), porque seria el valor obsoluto
    # (Es como medir una distancia, no existen medidas negativas, ya sea que se alejen del cero 0, o se acerquen)
    # Mientras mas se acerquen al 0 vamos a encontrar nuestra intercepcion en X y la raiz
    # Y para medir ese error, seria el Xu - Xi, pero como estamos tomando la mitad de cada uno de ellos..
    # Xu - Xi / 2 = Error Absoluto de calculo por cada iteracion

    # Primero sacamos el punto medio de nuestro intervalo
    # Calculamos el ERROR
    print("-" * 100)
    for i in range(iteraciones):
        
        Xr = ((Xi + Xu) / 2)
        error = ((Xu - Xi) /2)
        print(f"| Iteracion {i + 1} | Xi = {Xi:.6f}, Xu = {Xu:.6f} Xr = {Xr:.6f} | f(Xr) = {funcion(Xr):.6f} | Error = {error:.6f} |")
        print("-" * 100)
    # Esta cosa seguira iterando hasta el fin de los tiempo, pero necesitamos una orden de paro
    # Aqui es donde entra el valor del ERROR de calculo, si decimos que 0.000681 es relativamente muy cercano a 0
    # Entonces para las iteraciones,tambien por eso especificamos la TOLERANCIA de decimales, mientras mas pequeño sea esa TOLERANCIA
    # mas iteraciones hace y mas exacto sera el resultado, pero tambien depende de la cantidad de Iteraciones...
    
    #Estaras dispuesto a sacrificar, tiempo de ejecucion por el Valor mas exacto? io NO jsjsjs
    #En esta caso, la raiz se encuentra entre 14 y 15 aprox asi que no es tan necesario, con una la hacemos sjjsjs

    # SI el valor absoluto del Error es menor a la tolerancia, es decir  
    #  |-0.005207| < 0.031250
    #   0.005207 < 0.031250 Si       ,  la encontraste bro nice y se para y ya
        if abs(funcion(Xr)) < tolerancia:
            print(f"\n¡Raiz encontrada!!!\n\t>>>> Xr = {Xr:.6f} (f(Xr) = {funcion(Xr):.6f}) <<<<<")
            break
    
    # Ahora como necesitamos ver si se divide a la izquierda o a la derecha para los nuevos intervalos
    # Ya vimos que con la multiplicacion podemos verificar si esta la raiz cerca de esos puntos o NO
    # Por lo tanto utilizaremos esa misma idea para saber remplazar nuestras variables
    # Ejemplo:  
    #  funcion(Xi)⋅funcion(Xr) < 0 ( Xu=Xr ; Se mueve a la Izquierda)
    #  funcion(Xi)⋅funcion(Xr) > 0 (Xi=Xr  ; Se mueve a la Derecha)
    #  funcion(Xr) = 0.0000001 ; por decir (Ya encontraste la Raiz)  

        if funcion(Xi) * funcion(Xr) < 0:
            Xu = Xr  
        else:
            Xi = Xr  

def falsa_posicion():
    '''
    # La formula para el metodo de la falsa posicion es la siguiente:

    xr= xu- f(xu)(xi - xu)) /f(xi) - f(xu)

    Donde nuestros puntos a evaluar son xu y xi 
    despues evaluamos esos 2 puntos en la funcion orifinal
    para determinar el cambio de valores

    '''
    iteraciones = 100 # default de iteraciones
    Xi = float(input("Dame el valor de xi: ")) #Insercion de valor Xi
    Xu = float(input("Dame el valor de xu: ")) # Insercion de valor Xu
    iteraciones = int(input("(Por defecto: 100) Elije el numero de iteraciones: ")) # Insercion de cant.Iteraciones

    if iteraciones <= 0: # Sino es positivo el valor
        print("\nIntenta con valores positivos\n\t")#imprime un mensaje
        return  #No regresa nada
    elif iteraciones >= 1000000: #Si es mas de 1 millon, deja por default mil iteraciones
        iteraciones = 1000 # De nada xd
    tolerancia= float(input("Dame la Tolerancia por ejemplo(0.0001): ")) #Insercion de tolerancia para encontrar la RAIZ
    
    """
        Si la evaluacion de ambos puntos en la funcion funcion(Xi),funcion(Xu) es mayo o igual a cero,
        Esto quiere decir que no hay un salto o cambio de signo, por lo tanto no habra una raiz en esos
        intevalos, y avisara al usuario que no hay ninguna raiz....
    """
    if funcion(Xi) * funcion(Xu) >= 0:
        print(f"\n\tf(Xi)={Xi} * f(Xu)={Xu} = {funcion(Xi) * funcion(Xu)} \n\tNO EXISTE TAL RAIZ EN ESE INTERVALO...!\n\t") 
        return 
    print("-" * 75)

    """
        Xr_anterior, nos ayudara a almanecar el valor del intevalo Xr anterior, esto para poder realizar el cambio de
        los intervalos

    """
    Xr_anterior = 0
    for iteracion in range(iteraciones):
        """
            Calculamos el valor de Xr y despues lo evaluamos en la funcion
            Para checar el cambio de signo
        """
        Xr = Xu - (funcion(Xu) * (Xi - Xu)) / (funcion(Xi) - funcion(Xu))
        
        if iteracion > 0: #Para el resto de iteraciones sacamos el error
            error = abs((Xr - Xr_anterior) / Xr) * 100
        else:
            error = 100 # Para la primera, sera 100% de error

        print(f"| Iteracion {iteracion + 1} | Xi = {Xi:.6f}, Xu = {Xu:.6f} Xr = {Xr:.6f} | f(Xr) = {funcion(Xr):.6f} | Error = {error:.6f} |")
        print("-" * 100) # Imprimimos cada uno de los valores por separado los con'|'
        """
            Si al valor obsoluto de la funcion es menor a la tolerancia
            Esto quiere decir que estamos por debajo del rango que nos dio el usuario
            para encontrar la raiz.Ejemplo

            |-0.0058970|  < tolerancioa =0.01
            0.0058970<  = 0.01  ===> Entonces encontramos la raiz en base a la tolerancia 
            y regresa el valor de Xr para poder parar la iteracion

        """
        if abs(funcion(Xr)) < tolerancia: 
            print(f"\nRaiz encontrada: {Xr:.8f}")
            print(f"f({Xr:.8f}) = {funcion(Xr):.8f}")
            return Xr
        
        #Cambio de signo 
        if funcion(Xi) * funcion(Xr) < 0:
            Xu = Xr
        else:
            Xi = Xr
        Xr_anterior = Xr

def funcion(C):
    termino_1 = (667.38/C)
    termino_2 = (1 - math.exp(-0.14843 * C))
    final= (termino_1 * termino_2)-40
    return final

def main():
    while True:
        print("\n" + "="*50)
        print("       METODOS NUMERICOS - ENCONTRAR RAÍCES")
        print("="*50)
        print("1. Metodo de Biseccion")
        print("2. Metodo de la Falsa Posicion")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opcion (1-3): ")
        
        if opcion == "1":
            biseccion()
        elif opcion == "2":
            falsa_posicion()
        elif opcion == "3":
            print("Bye\n")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    main()