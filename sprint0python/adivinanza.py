print ("")
print ("Te sirven para escribir, dibujar, señalar y sentir, qué son?")
solucion = input ("a. Un lapiz b.Los dedos c.Los pies")
print ("")
puntuacion=0
if (solucion != 'b'):
    print ("Perdiste. Esa respuesta no es la correcta.\n")
    puntuacion = puntuacion - 5
else:
    print("¡Acertaste!.\n")
    puntuacion = puntuacion + 10
print ("Cuando llueve y sale el sol, todos los colores tengo yo. Qué soy?")
solucion = input ("a.Una nuve b.La luna c.Un arcoiris")
if (solucion != 'c'):
    print ("Perdiste. Esa respuesta no es la correcta.\n")
    puntuacion = puntuacion - 5
else:
    print("¡Acertaste!.\n")
    puntuacion = puntuacion + 10
print ("Blanca por dentro, verde por fuera. Si no sabes, espera. Qué soy?")
solucion = input ("a.Una pera b.Una manzana c.Una oreo")
if (solucion != 'a'):
    print ("Perdiste. Esa respuesta no es la correcta.\n")
    puntuacion = puntuacion - 5
else:
    print("¡Acertaste!.\n")
    puntuacion = puntuacion + 10

print ("Fin del juego. La puntuación total es: "+str(puntuacion))

