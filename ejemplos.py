#while i <= n:
#    print(i)
#    i = i +1

#i = 0
#for i in range(11):
#    print(i)

#i = 0
#for i in range(4, 13, 4):
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

subtotal = 0
productos = int(input("Cuantos Productos va a ingresar?: "))
while productos < 0:
    print("Error, no se pueden ingresar numeros negativos, intente de nuevo.")
    productos = int(input("Cuantos Productos va a ingresar?: "))
for i in range(productos):
    precio = int(input("Ingrese el precio del producto: "))
    subtotal += precio
if subtotal > 50000:
    descuento = subtotal * 0.1
    print("El total con descuento es: ", subtotal - descuento)
else:
    print("El total a pagar es: ", subtotal)