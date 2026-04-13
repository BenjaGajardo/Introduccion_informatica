#while i <= n:
#    print(i)
#    i = i +1

#i = 0
#for i in range(11):
#    print(i)

#i = 0
#for i in range(10,0,-1):
#    print(i)

#print("Inicio")
#for i in "hector":
#    print("hola")
#    print(i)
#print("Fin")

#print("Inicio")
#for i in range(3):
#    print("hola")
#print("Fin")

#print("inicio")
#for i in range(1, 12, 2):
#    print("hola")
#print("Fin")

#print("Inicio")
#for i in range(2, 10):
#    print("hola")
#    print(i)
#print("Fin")


#for i in range(5):
#    print("A: " + str(i))

#for i in range(3, 5):
#    print("B: " + str(i))

#for i in range(5, 3, -1):
#    print("C: " + str(i))


#for i in range(1, 4):
#    print(i)

#2. del 1 al 10 (forma intuitiva)
#print("\nNumeros del 1 al 10")
#for i in range(1, 11):
#    print(i)

#3. del 1 al 10 (Forma basaada en el indice 0)
#print("\nNumeros del 1 al 10 (2da version)")
#for i in range(0, 10):
#    print(i + 1)

#4. Saltos (Step positivo)
#print("\nCuenta de dos en dos")
#for i in range(0, 10, 2):
#    print(i)

#5. Reversa (step negativo)
#print("\nCuenta regresiva")
#El limite es 0 (el muro), por lo tanto se detiene en 1.
#for i in range(10, 0, -1):
#    print(i)

#subtotal = 0
#productos = int(input("Cuantos Productos va a ingresar?: "))
#while productos < 0:
#    print("Error, no se pueden ingresar numeros negativos, intente de nuevo.")
#    productos = int(input("Cuantos Productos va a ingresar?: "))
#for i in range(productos):
#    precio = int(input("Ingrese el precio del producto: "))
#    subtotal += precio
#if subtotal > 50000:
#    descuento = subtotal * 0.1
#    print("El total con descuento es: ", subtotal - descuento)
#else:
#    print("El total a pagar es: ", subtotal)



#i = 0
#for i in range(1,11,1):
#    print(i)

#suma = 0
#for i in range(1, 11):
#    suma = suma + i
#    print(suma)

#for i in range(1, 21):
#    if i % 2 == 0:
#        print(i)

#for i in range(1, 401):
#    if i % 2 != 0:
#        print(i)

#for i in range(1, 101):
#    if i % 3 == 0:
#        print("Cueck")
#    else:
#        print(i)


#for i in range(1000):
#    pregunta = int(input("Ingrese el numero para verificar si es par: "))
#    if pregunta % 2 == 0:
#        print("Es par")
#    else:
#        print("Es impar")
#    pregunta2 = input("¿Desesa ingresar otro numero? (s/n): ")
#    if pregunta2.lower() == "n" or pregunta2.lower() == "N":
#        print("Muchas gracias")
#        break
#    elif pregunta2.lower() == "s" or pregunta2.lower() == "S":
#        print("Continuemos...")
#    else:
#        print("Error debe ingresar una respuesta valida")
#        break


#suma_numeros = 0
#for i in range(30):
#    numeros = int(input(f"Ingrese el {i+1} numero: "))
#    suma_numeros = suma_numeros + numeros
#promedio = suma_numeros / 30
#print("El promedio de los 30 numeros es",promedio)

#pregunta = int(input("Ingrese el numero: "))
#while pregunta <= 0:
#    print("Error no debe ser negativo")
#    pregunta = int(input("Ingrese el numero: "))
#area = 3.14 * pregunta**2
#print("El area es", area)
#pregunta2 = input("Desea ingresar otro numero? (s/n): ")
#while pregunta2 == "s":
#    pregunta = int(input("Ingrese el numero: "))
#    while pregunta <= 0:
#        print("Error no debe ser negativo")
#        pregunta = int(input("Ingrese el numero: "))
#    area = 3.14 * pregunta**2
#    print("El area es", area)
#    pregunta2 = input("Desea ingresar otro numero? (s/n): ")
#print("Muchas gracias")


#base = int(input("Ingrese la base: "))
#altura = int(input("Ingrese la altura: "))
#while base <= 0 or altura <= 0:
#    print("Error los digitos deben ser positivos")
#    base = int(input("Ingrese la base: "))
#    altura = int(input("Ingrese la altura: "))
#area = base * altura
#print("El area es", area)
#pregunta = input("¿Desea calcular otra base? (s/n): ")
#while pregunta == "s":
#    base = int(input("Ingrese la base: "))
#    altura = int(input("Ingrese la altura: "))
#    while base <= 0 or altura <= 0:
#        print("Error los digitos deben ser positivos")
#        base = int(input("Ingrese la base: "))
#        altura = int(input("Ingrese la altura: "))
#    area = base * altura
#    print("El area es", area)
#    pregunta = input("¿Desea calcular otra base? (s/n): ")
#print("Muchas gracias")


#radio = int(input("Ingrese el radio: "))
#while radio <= 0:
#    print("Error el digito debe ser positivo")
#    radio = int(input("Ingrese el radio: "))
#volumen = (4/3) * 3.14 * radio**3
#print("El area es", volumen)
#pregunta = input("¿Desea calcular otro volumen? (s/n): ")
#while pregunta == "s":
#    radio = int(input("Ingrese el radio: "))
#    while radio <= 0 :
#        print("Error el digito debe ser positivo")
#        radio = int(input("Ingrese el radio: "))
#    volumen = (4/3) * 3.14 * radio**3
#    print("El area es", volumen)
#    pregunta = input("¿Desea calcular otro volumen? (s/n): ")
#print("Muchas gracias")


lado = int(input("Ingrese el lado: "))
while lado <= 0:
    print("Error el digito debe ser positivo")
    lado = int(input("Ingrese el lado: "))
area_total = 6 * lado**2
perimetro = 12 * lado
print("El area es", area_total)
print("El perimetro es", perimetro)
pregunta = input("¿Desea calcular otro? (s/n): ")
while pregunta == "s":
    lado = int(input("Ingrese el lado: "))
    while lado <= 0:
        print("Error el digito debe ser positivo")
        lado = int(input("Ingrese el lado: "))
    area_total = 6 * lado**2
    perimetro = 12 * lado
    print("El area es", area_total)
    print("El perimetro es", perimetro)
    pregunta = input("¿Desea calcular otro? (s/n): ")
print("Muchas gracias")

