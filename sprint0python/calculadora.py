from operaciones import suma,resta,multiplicacion, division
repetir = "s"
while repetir == "s":
    numero1 = int(input("Introduzca el primer número: "))
    numero2 = int(input("Introduzca el segundo número: "))
    operacion = input ("Indique qué operación desea realizar")
    if operacion == "suma":
        opSolucion=suma(numero1,numero2)
        print("El resultado es...: "+str(opSolucion))
    elif operacion == "resta":
            opSolucion=resta(numero1,numero2)
            print("El resultado es...: "+str(opSolucion))
    elif operacion == "multiplicación":
                opSolucion=multiplicacion(numero1,numero2)
                print("El resultado es...: "+str(opSolucion))
    elif operacion == "división":
                     opSolucionSol = division(numero1,numero2)
                     print("El resultado es...: "+str(opSolucion))
    if numero1==0 or numero2==0:
            repetir = input("\n¿Desea utilizar de nuevo la calculadora? (s/n): ")
            print("\nEl resultado de su operación es: "+str(opSolucion))

    repetir = input("\n¿Desea utilizar de nuevo la calculadora? (s/n): ")
        
            
