try:
    diaMes = int(input("Dime el número de mes: "))
    if diaMes in [1, 3, 5, 7, 8, 10, 12]:
        print("Este mes tiene 31 días")
    elif diaMes in [4, 6, 9, 11]:
        print("Este mes tiene 30 días")
    else:
        print("Este mes tiene 28 días")
except ValueError:
    print("Hay algún error en el código")
finally:
    print("Programa terminado")
