#medida = float(input("Ingrese la medida en centímetros: "))
#medida_kilometros = medida / 100000
#medida_metros = medida / 100
#medida_centimetros = medida
#print("\nResultados: ")
#print(f"Kilómetros: {medida_kilometros}")
#print(f"Metros: {medida_metros}")
#print(f"Centímetros: {medida_centimetros}")
#pregunta = input("\n¿Desea convertir otra medida? (si/no): ")
#while pregunta == "si":
#    medida = float(input("Ingrese la medida en centímetros: "))
#    medida_kilometros = medida / 100000
#    medida_metros = medida / 100
#    medida_centimetros = medida
#    print("\nResultados: ")
#    print(f"Kilómetros: {medida_kilometros}")
#    print(f"Metros: {medida_metros}")
#    print(f"Centímetros: {medida_centimetros}")
#    pregunta = input("\n¿Desea covertir otra medida? (si/no): ")
#print("¡Gracias por usar el programa de conversión de medidas!")


#print("Impresora de numeros del 1 al 10")
#i = 1
#while i <= 10:
#    print(i)
#    i = i + 1


#print("Suma de numeros del 1 al 10")
#i = 1
#suma = 0
#while i <= 10:
#    suma = suma + i
#    i = i + 1
#print("\nLa suma de los numeros del 1 al 10 es", suma)


#numero = int(input("Ingrese un numero: "))
#if numero %2 == 0:
#    print("Es par")
#else:
#    print("Es impar")
#pregunta = input("Desea ingresar otro numero? (s/n): ")
#while pregunta == "s":
#    numero = int(input("Ingrese otro numero: "))
#    if numero %2 == 0:
#        print("Es par")
#        pregunta = input("Desea ingresar otro numero? (s/n): ")
#    else:
#        print("Es impar")
#        pregunta = input("Desea ingresar otro numero? (s/n): ")
#print("¡Muchas gracias por usar el programa!")


#numeros = int(input("Ingrese el primer numero: "))
#suma = 0
#contador = 0
#while contador < 30:
#    suma = suma + numeros
#    contador = contador + 1
#    if contador < 30:
#        numeros = int(input("Ingrese otro numero: "))
#        promedio = suma / contador
#print("\nEL promedio de los numero ingresados es", promedio)


#print("Impresora de numeros pares del 0 al 20")
#contador = 1
#while contador <= 20:
#    print(contador)
#    contador = contador + 2


#print("Suma de numeros pares del 1 al 400")
#contador = 2
#suma = 0
#while contador <= 400:
#    suma = suma + contador
#    contador = contador + 2
#print("\nLa suma de los numeros pares del 1 al 400 es", suma)


#radio_circulo = int(input("Ingrese el radio del círculo: "))
#if radio_circulo > 0:
#    area = 3.1416 * radio_circulo ** 2
#    print("\nEl área del círculo es", area)
#else:
#    print("Error, el radio debe ser un número positivo.")
#pregunta = input("\n¿Desea calcular el área de otro círculo? (si/no): ")
#while pregunta == "si":
#    radio_circulo = int(input("Ingrese el radio del círculo: "))
#    if radio_circulo > 0:
#        area = 3.1416 * radio_circulo ** 2
#        print("\nEl área del círculo es", area)
#        pregunta = input("\n¿Desea calcular el área de otro círculo? (si/no): ")
#    else:
#        print("Error, el radio debe ser un número positivo.")
#        pregunta = input("\n¿Desea calcular el área de otro círculo? (si/no): ")
#print("¡Gracias por usar el programa de cálculo de áreas de círculos!")


#radio_circulo = int(input("Ingrese el radio del círculo: "))
#if radio_circulo > 0:
#    perimetro = 2 * 3.1416 * radio_circulo
#    print("\nEl perímetro del círculo es", perimetro)
#else:
#    print("Error, el radio debe ser un número positivo.")
#pregunta = input("\n¿Desea calcular el perímetro de otro círculo? (si/no): ")
#while pregunta == "si":
#    radio_circulo = int(input("Ingrese el radio del círculo: "))
#    if radio_circulo > 0:
#        perimetro = 2 * 3.1416 * radio_circulo
#        print("\nEl perímetro del círculo es", perimetro)
#        pregunta = input("\n¿Desea calcular el perímetro de otro círculo? (si/no): ")
#    else:
#        print("Error, el radio debe ser un número positivo.")
#        pregunta = input("\n¿Desea calcular el perímetro de otro círculo? (si/no): ")
#print("¡Gracias por usar el programa de cálculo de perímetros de círculos!")


#radio_circulo = int(input("Ingrese el radio del círculo: "))
#if radio_circulo > 0:
#    volumen = (4/3) * 3.1416 * radio_circulo ** 3
#    print("\nEl volumen del círculo es", volumen)
#else:
#    print("Error, el radio debe ser un número positivo.")
#pregunta = input("\n¿Desea calcular el volumen de otro círculo? (si/no): ")
#while pregunta == "si":
#    radio_circulo = int(input("Ingrese el radio del círculo: "))
#    if radio_circulo > 0:
#        volumen = (4/3) * 3.1416 * radio_circulo ** 3
#        print("\nEl volumen del círculo es", volumen)
#        pregunta = input("\n¿Desea calcular el volumen de otro círculo? (si/no): ")
#    else:
#        print("Error, el radio debe ser un número positivo.")
#        pregunta = input("\n¿Desea calcular el volumen de otro círculo? (si/no): ")
#print("¡Gracias por usar el programa de cálculo de volúmenes de círculos!")


#lado_cuadrado = int(input("Ingrese la longitud del lado del cuadrado: "))
#if lado_cuadrado > 0:
#    area = 6 * lado_cuadrado ** 2
#    perimetro = 12 * lado_cuadrado
#    print("\nEl área del cuadrado es", area)
#    print("El perímetro del cuadrado es", perimetro)
#else:
#    print("Error, el lado debe ser un número positivo.")
#pregunta = input("\n¿Desea calcular el area y perímetro de otro cuadrado? (si/no): ")
#while pregunta == "si":
#    lado_cuadrado = int(input("Ingrese la longitud del lado del cuadrado: "))
#    if lado_cuadrado > 0:
#        area = 6 * lado_cuadrado ** 2
#        perimetro = 12 * lado_cuadrado
#        print("\nEl área del cuadrado es", area)
#        print("El perímetro del cuadrado es", perimetro)
#        pregunta = input("\n¿Desea calcular el area y perímetro de otro cuadrado? (si/no): ")
#    else:
#        print("Error, el lado debe ser un número positivo.")
#        pregunta = input("\n¿Desea calcular el area y perímetro de otro cuadrado? (si/no): ")
#print("¡Gracias por usar el programa de cálculo de areas y perímetros de cuadrados!")


#print("Impresora de numero del 1 al 100 omitiendo los múltiplos de 3")
#contador = 1
#while contador <= 100:
#    if contador % 3 != 0:
#        print(contador)
#        contador = contador + 1
#    else:
#        contador = contador + 1


#print("Impresora de numero del 1 al 100 omitiendo los múltiplos de 5")
#contador = 1
#while contador <= 100:
#    if contador % 5 != 0:
#        print(contador)
#        contador = contador + 1
#    else:
#        contador = contador + 1


#print("Impresora de numero del 1 al 100 omitiendo los múltiplos de 5 y 3")
#contador = 1
#while contador <= 100:
#    if contador % 5 != 0 and contador %3 != 0:
#        print(contador)
#        contador = contador + 1
#    else:
#        contador = contador + 1


#print("Impresora de numero del 1 al 100 reemplazando los múltiplos 3 por Cuek")
#contador = 1
#while contador <= 100:
#    if contador % 3 == 0:
#        print("Cuek")
#    else:
#        print(contador)
#    contador = contador + 1


#numero = int(input("Ingrese un numero para calcular su factorial: "))
#if numero < 0:
#    print("Error: el número debe ser positivo.")
#else:
#    factorial = 1
#    contador = 1
#    while contador <= numero:
#        factorial = factorial * contador
#        contador += 1
#    print("El factorial de", numero, "es:", factorial)
#    pregunta = input("Desea calcular nuevamente? (s/n): ")
#    while pregunta == "s":
#        numero = int(input("Ingrese un numero para calcular su factorial: "))
#        if numero < 0:
#            print("Error: el número debe ser positivo.")
#        else:
#            factorial = 1
#            contador = 1
#            while contador <= numero:
#                factorial = factorial * contador
#                contador += 1
#            print("El factorial de", numero, "es:", factorial)
#            pregunta = input("Desea calcular nuevamente? (s/n): ")
#    print("¡Gracias por usar el programa de cálculo de factoriales!")




#numero = int(input("Ingrese un número para contar sus dígitos: "))
#if numero < 0:
#    print("Error: el número debe ser positivo.")
#else:
#    contador = 0
#    while numero > 0:
#        numero = numero // 10
#        contador += 1
#    print("El número tiene", contador, "dígitos.")
#    pregunta = input("Desea calcular nuevamente? (s/n): ")
#    while pregunta == "s":
#        numero = int(input("Ingrese un número para contar sus dígitos: "))
#        if numero < 0:
#            print("Error: el número debe ser positivo.")
#        else:
#            contador = 0
#            while numero > 0:
#                numero = numero // 10
#                contador += 1
#            print("El número tiene", contador, "dígitos.")
#            pregunta = input("Desea calcular nuevamente? (s/n): ")
#    print("¡Gracias por usar el programa de conteo de dígitos!")


#lado_cuadrado = int(input("Ingrese la longitud del lado del cuadrado: "))
#if lado_cuadrado > 0:
#    area = lado_cuadrado ** 2
#    perimetro = 4 * lado_cuadrado
#    print("\nEl área del cuadrado es", area)
#    print("El perímetro del cuadrado es", perimetro)
#else:
#    print("Error, el lado debe ser un número positivo.")
#pregunta = input("\n¿Desea calcular el area y perímetro de otro cuadrado? (si/no): ")
#while pregunta == "si":
#    lado_cuadrado = int(input("Ingrese la longitud del lado del cuadrado: "))
#    if lado_cuadrado > 0:
#        area = lado_cuadrado ** 2
#        perimetro = 4 * lado_cuadrado
#        print("\nEl área del cuadrado es", area)
#        print("El perímetro del cuadrado es", perimetro)
#        pregunta = input("\n¿Desea calcular el area y perímetro de otro cuadrado? (si/no): ")
#    else:
#        print("Error, el lado debe ser un número positivo.")
#        pregunta = input("\n¿Desea calcular el area y perímetro de otro cuadrado? (si/no): ")
#print("¡Gracias por usar el programa de cálculo de areas y perímetros de cuadrados!")


numero = int(input("Ingrese un numero para calcular su potencia sin usar el operador **: "))
potencia = int(input("Ingrese el exponente: "))
if numero < 0 or potencia < 0:
    print("Error: el número y el exponente deben ser positivos.")
else:
    resultado = 1
    contador  = 1
    while contador <= potencia: 
        resultado = resultado * numero
        contador += 1
    print("El resultado de", numero, "elevado a la potencia", potencia, "es:", resultado)
    pregunta = input("Desea calcular nuevamente? (s/n): ")
    while pregunta == "s":
        numero = int(input("Ingrese un numero para calcular su potencia sin usar el operador **: "))
        potencia = int(input("Ingrese el exponente: "))
        if numero < 0 or potencia < 0:
            print("Error: el número y el exponente deben ser positivos.")
        else:
            resultado = 1
            contador  = 1
            while contador <= potencia: 
                resultado = resultado * numero
                contador += 1
            print("El resultado de", numero, "elevado a la potencia", potencia, "es:", resultado)
            pregunta = input("Desea calcular nuevamente? (s/n): ")
    print("¡Gracias por usar el programa de cálculo de potencias!")
