def suma (numero1, numero2):
    return numero1+numero2
def resta (numero1,numero2):
    if numero1<numero2:
        return numero2-numero1
    else:
        return numero1-numero2

def multiplicacion (numero1,numero2):
    return numero1*numero2
def division (numero1,numero2):
    if numero1==0 or numero2==0:
        return print("No se puede dividir entre 0")
    else: 
        return numero1/numero2