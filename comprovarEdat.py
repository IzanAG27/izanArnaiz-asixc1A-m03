"""
Izan Arnaiz Gallego
17/09/2023, 18/09/2023
ASIXc M03 UF1 A1
Descripció:
Estructura d'un programa informàtic - Algoritmes - Git
"""

# Este ejercicio está hecho para saber si una persona es mayor o menor de edad.

#Preguntamos al usuario que edad tiene
comprovarEdat = int(input("¿Que edad tienes? "))

"""
Establecemos una condición, si tiene 18 años o más, es mayor de edad,por ende,
si tiene menos, es menor de edad, en ambos casos, finalizará el programa.
"""
if comprovarEdat >= 18:
    print("Eres mayor de edad.")
    print("... Programa finalizado ...")
else:
    print("Eres menor de edad.")
    print("... Programa finalizado ...")

