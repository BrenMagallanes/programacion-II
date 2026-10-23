import math


def ganancia_parabolica(frecuencia, diametro):
    longdeonda = 300000000/(frecuencia * (10**9))
    ganancia = 10*(math.log10((0, 55)*((math.pi * diametro)/longdeonda)**2))
    return ganancia



def main():
    print()
