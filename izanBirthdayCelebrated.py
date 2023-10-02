"""
    Izan Arnaiz Gallego
    02/10/2023
    ASIXc M03 UF1 A2 Manipulació dades
"""

diaAniversari = int(input("Que dia cumples años?: "))
mesAniversari = int(input("Que mes cumples años?: "))
diaActual = int(input("Que día es hoy?: "))
mesActual = int(input("En que mes estamos?: "))

if mesActual >= mesAniversari and diaActual > diaAniversari:
    print("Ya lo has celebrado!")
elif mesActual == mesAniversari and diaActual == diaAniversari:
    print("Felicidades :)")
else:
    print("No has celebrado tu cumpleaños")