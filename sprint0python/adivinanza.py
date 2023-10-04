import random

puntos = 0
veces = 0

adivinanzas = {
    1: "Te sirven para escribir, dibujar, señalar y sentir, qué son? a. Un lapiz b.Los dedos c.Los pies",
    2: "Cuando llueve y sale el sol, todos los colores tengo yo. Qué soy? a.Una nuve b.La luna c.Un arcoiris",
    3: "Blanca por dentro, verde por fuera. Si no sabes, espera. Qué soy? a.Una pera b.Una manzana c.Una oreo",
}

claves_adivinanzas = list(adivinanzas.keys())

while veces < 3:
    sel = random.sample(claves_adivinanzas, 1)[0]
    claves_adivinanzas.remove(sel) 

    print(adivinanzas[sel])
    sol = input("\t")
    veces += 1

    if sel == 1:
        if sol == 'b':
            print("\n¡Enhorabuena! Has acertado.\n")
            puntos += 10
        else:
            print("\nError. Esa es la respuesta incorrecta.\n")
            puntos -= 5
    elif sel == 2:
        if sol == 'c':
            print("\n¡Enhorabuena! Has acertado.\n")
            puntos += 10
        else:
            print("\nError. Esa es la respuesta incorrecta.\n")
            puntos -= 5
    elif sel == 3:
        if sol == 'a':
            print("\n¡Enhorabuena! Has acertado.\n")
            puntos += 10
        else:
            print("\nError. Esa es la respuesta incorrecta.\n")
            puntos -= 5

print("Ha finalizado el juego. Felicidades, tienes un total de: " + str(puntos) + "\n")