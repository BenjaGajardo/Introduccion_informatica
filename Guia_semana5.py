i = 0
for i in range (1, 11, 1):
    print(i)


suma = 0
for i in range(1, 11):
    suma = suma + i
    print(suma)


i = 0
for i in range(2, 21, 2):
    print(i)


suma = 0
for i in range(1, 401):
    if i % 2 != 0:
        suma = suma + i
print(suma)


for i in range(1, 101):
    if i % 3 == 0:
        print("Cuek")
    else:
        print(i)


for i in range(1000): 
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
    pregunta = input("Desea ingresar otro numero? (s/n): ")
    if pregunta.lower() == "n" or pregunta.lower() == "no":
        print("Gracias por usar el programa")
        break
    elif pregunta.lower() == "s" or pregunta.lower() == "si":
        print("Continuemos...")
    else:
        print("Error, se esperaba una respuesta afirmativa o negativa.")
        break


numeros = int(input("Ingrese el primer numero: "))
suma = 0
contador = 0
for i in range(1, 30):
    suma = suma + numeros
    contador = contador + 1
    if contador < 30:
        numeros = int(input("Ingrese otro numero: "))
        promedio = suma / contador
print("\nEL promedio de los numero ingresados es", promedio)


radio_circulo = int(input("Ingrese el radio del círculo: "))
if radio_circulo > 0:
    area = 3.1416 * radio_circulo ** 2
    print("\nEl área del círculo es", area)
else:
    print("Error, el radio debe ser un número positivo.")
pregunta = input("\n¿Desea calcular el área de otro círculo? (si/no): ")
while pregunta == "si":
    radio_circulo = int(input("Ingrese el radio del círculo: "))
    if radio_circulo > 0:
        area = 3.1416 * radio_circulo ** 2
        print("\nEl área del círculo es", area)
        pregunta = input("\n¿Desea calcular el área de otro círculo? (si/no): ")
    else:
        print("Error, el radio debe ser un número positivo.")
        pregunta = input("\n¿Desea calcular el área de otro círculo? (si/no): ")
print("¡Gracias por usar el programa de cálculo de áreas de círculos!")


Base_rectangulo = int(input("Ingrese la base del rectángulo: "))
Altura_rectangulo = int(input("Ingrese la altura del rectángulo: "))
if Base_rectangulo > 0 and Altura_rectangulo > 0:
    area = Base_rectangulo * Altura_rectangulo
    print("\nEl área del rectángulo es", area)
else:
    print("Error, la base y la altura deben ser números positivos.")
pregunta = input("\n¿Desea calcular el área de otro rectángulo? (si/no): ")
while pregunta == "si":
    Base_rectangulo = int(input("Ingrese la base del rectángulo: "))
    Altura_rectangulo = int(input("Ingrese la altura del rectángulo: "))
    if Base_rectangulo > 0 and Altura_rectangulo > 0:
        area = Base_rectangulo * Altura_rectangulo
        print("\nEl área del rectángulo es", area)
        pregunta = input("\n¿Desea calcular el área de otro rectángulo? (si/no): ")
    else:
        print("Error, la base y la altura deben ser números positivos.")
        pregunta = input("\n¿Desea calcular el área de otro rectángulo? (si/no): ")
print("¡Gracias por usar el programa de cálculo de áreas de rectángulos!")


radio_esfera = int(input("Ingrese el radio de la esfera: "))
if radio_esfera > 0:
    volumen_esfera = (4/3) * 3.1416 * (radio_esfera ** 3)
    print("El volumen de la esfera es", volumen_esfera)
else:
    print("Error, el radio debe ser un número positivo.")
pregunta = input("\n¿Desea calcular el volumen de otra esfera? (si/no): ")
while pregunta == "si":
    radio_esfera = int(input("Ingrese el radio de la esfera: "))
    if radio_esfera > 0:
        volumen_esfera = (4/3) * 3.1416 * (radio_esfera ** 3)
        print("El volumen de la esfera es", volumen_esfera)
        pregunta = input("\n¿Desea calcular el volumen de otra esfera? (si/no): ")
    else:
        print("Error, el radio debe ser un número positivo.")
        pregunta = input("\n¿Desea calcular el volumen de otra esfera? (si/no): ")
print("¡Gracias por usar el programa de cálculo de volúmenes de esferas!")


radio_circulo = int(input("Ingrese el radio del círculo: "))
if radio_circulo > 0:
    perimetro = 2 * 3.1416 * radio_circulo
    print("\nEl perímetro del círculo es", perimetro)
else:
    print("Error, el radio debe ser un número positivo.")
pregunta = input("\n¿Desea calcular el perímetro de otro círculo? (si/no): ")
while pregunta == "si":
    radio_circulo = int(input("Ingrese el radio del círculo: "))
    if radio_circulo > 0:
        perimetro = 2 * 3.1416 * radio_circulo
        print("\nEl perímetro del círculo es", perimetro)
        pregunta = input("\n¿Desea calcular el perímetro de otro círculo? (si/no): ")
    else:
        print("Error, el radio debe ser un número positivo.")
        pregunta = input("\n¿Desea calcular el perímetro de otro círculo? (si/no): ")
print("¡Gracias por usar el programa de cálculo de perímetros de círculos!")


lado_cubo = int(input("Ingrese el lado del cubo: "))
if lado_cubo > 0:
    area_total = 6 * (lado_cubo ** 2)
    perimetro = lado_cubo * 12
    print("\nEl área total del cubo es", area_total)
    print("El volumen del cubo es", perimetro)
else:
    print("Error, el radio debe ser un número positivo.")
pregunta = input("\n¿Desea calcular el area total y perímetro de otro cubo? (si/no): ")
while pregunta == "si":
    lado_cubo = int(input("Ingrese el lado del cubo: "))
    if lado_cubo > 0:
        area_total = 6 * (lado_cubo ** 2)
        perimetro = lado_cubo * 12
        print("\nEl área total del cubo es", area_total)
        print("El volumen del cubo es", perimetro)
        pregunta = input("\n¿Desea calcular el area total y perímetro de otro cubo? (si/no): ")
    else:
        print("Error, el radio debe ser un número positivo.")
        pregunta = input("\n¿Desea calcular el area total y perímetro de otro cubo? (si/no): ")
print("¡Gracias por usar el programa de cálculo de áreas y perímetros de cubos!")


while True:
    numero = input("Ingresa un número: ")
    contador = 0
    for i in numero:
        contador += 1
    print("Cantidad de dígitos:", contador)
    respuesta = input("¿Desea ingresar otro número? (s/n): ").lower()
    if respuesta == "n" or respuesta == "no":
        break
print("¡Gracias por usar el programa!")


