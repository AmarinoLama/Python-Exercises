prueba = "hola mundo"

try:
    print(prueba + 3)
except TypeError:
    print("el programa ha fallado")
finally:
    print("fin del programa")