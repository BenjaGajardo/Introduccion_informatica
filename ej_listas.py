#lista = []
#lista = input("Ingrese los elementos de la lista: ")
#print(lista)

#notas = [5.5, 6.0, 4.8, 7.0, 5.0]
#print(type(notas))
#print(notas[0])
#print(notas[4])
#print(notas[-4])
#print(notas[-3])
#print(type(notas[0]))
#print(type(notas[4]))
#print(type(notas[-1]))
#print(type(notas[-2]))

#lista_tipos = ["benja", 4.5, 2]
#print("\nlista tipos:")
#print(type(lista_tipos))

#nombres = ['Ana', 'Luis', 'Maria', 'Jorge', 'Sofia']
#print(nombres[ 1:3 ])
#print(nombres[ 0:2 ])
#print(nombres[ 2:5 ])
#print(nombres[ : ])


#numeros = [5, 12, 7, 20, 33, 18, 2, 45]
#print(numeros[ 2:6 ])
#print(numeros[ 0:4 ])
#print(numeros[ 3: ])
#suma = numeros[3] + numeros[5]
#print(suma)

#numeros = [5, 12, 7, 20, 33, 18, 2, 45]
#variable = numeros[ 0:7:2 ]
#print(variable)

#numeros = [5, 12, 7, 20, 33, 18, 2, 45]
#variable = numeros[ 1:8:3 ]
#print(variable)

#numeros = [5, 12, 7, 20, 33, 18, 2, 45]
#numeros.reverse()
#variable = numeros
#print(numeros)

#frutas = ['manzana', 'pera', 'uva', 'cereza']
# Forma 1: Iteración directa (más pythónica)
#for fruta in frutas:
#    print(fruta)
# Forma 2: Iteración con índice usando range y len
#for i in range(len(frutas)):
#    print(f"Posición {i}: {frutas[i]}")


#compras = []
#for i in range(5):
#    solicitar = input(f"Ingrese la {i} fruta: ")
#    compras.append(solicitar)
#print(compras)
#print(compras[0])
#print(compras[4])
#contar = len(compras)
#print(contar)

#temps = [18.5, 22.0, 15.3, 28.7, 19.1, 25.0]
#temps.sort()
#print(temps)
#temps.append(30.2)
#print(temps)
#temps.remove(15.3)
#print(temps)
#print(max(temps))
#print(min(temps))
#promedio = sum(temps) / len(temps)
#print(promedio)


#compras = []
#for i in range(5):
#    productos = input(f"Ingrese el {i+1} producto: ")
#    compras.append(productos)
#print("Lista completa:")
#print(compras)
#print("Primer y ultimo elemento:")
#print(compras[0], compras[-1])
#print("Total que hay en la lista:")
#print(len(compras))


#notas = []
#cuantas = int(input("¿Cuantas notas va a promediar?: "))
#for i in range (cuantas):
#    calificaciones = int(input(f"Ingrese la {i+1} nota: "))
#    notas.append(calificaciones)
#promedio = sum(notas) / len(notas)
#print("Nota maxima:")
#print(max(notas))
#print("Nota minima:")
#print(min(notas))
#print("Promedio total:")
#print(promedio)


#notas = []
#aprobados = []
#reprobados = []
#cuantas = int(input("¿Cuantas notas va a promediar?: "))
#for i in range(cuantas):
#    calificaciones = float(input(f"Ingrese la {i+1} nota: "))
#    notas.append(calificaciones)
#    if calificaciones > 4.0:
#        aprobados.append(calificaciones)
#    else:
#        reprobados.append(calificaciones)
#promedio = sum(notas) / len(notas)
#print("Aprobados:")
#print(len(aprobados))
#print("Reprobados:")
#print(len(reprobados))
#print("Nota maxima:")
#print(max(notas))
#print("Nota minima:")
#print(min(notas))
#print("Promedio total:")
#print(promedio)
"""
nombres = ["Ana", "Luis", "María", "Jorge", "Sofía"]
notas = [5.8, 4.2, 6.7, 3.9, 5.1]
buscar = input("¿Que estudiante desea buscar?: ")
if buscar in nombres: 
    indice = nombres.index(buscar)
    nota = notas[indice]
    print(f"{buscar} tiene nota {nota}")
else:
    print("Estudiante no encontrado")
"""
"""
lista = []
pregunta = int( input("¿Cuantos numeros desea ingresar?: "))
for i in range(pregunta):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    lista.append(numero)
suma_total = sum(lista)
promedio_lista = suma_total / len(lista)
print(f"la suma total de los numeros es: {suma_total}")
print(f"el promedio de los numeros es: {promedio_lista}")
"""

"""
lista = []
mayor = 0
menor = 100
for i in range(7):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    if numero > mayor:
        mayor = numero
    elif numero < menor:
        menor = numero
    lista.append(numero)
print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")
"""

"""
lista = []
pares = 0
impares = 0
for  i in range(10):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1 
    lista.append(numero)
print(f"Los numeros pares son: {pares}")
print(f"Los numeros impares son: {impares}")
"""

"""
lista = []
for i in range(5):
    nombres = input(f"Ingrese el nombre del estudiante {i+1}: ")
    lista.append(nombres)
pregunta = input("¿Desea buscar un estudiante? (s/n): ")
if pregunta == "s":
    buscar = input("¿Que estudiante desea buscar?: ")
    for i in range(len(lista)):
        if lista[i] == buscar:
            print(f"{buscar} se encuentra en la posicion {i}")
            break
    else:
        print("Estudiante no encontrado")
else:
    print("Gracias por usar el programa")
"""

"""
numeros = []
def calcular_promedio(numeros):
    if len(numeros) == 0:
        return 0
    else:
        return sum(numeros) / len(numeros)

pregunta = int(input("¿Cuantos numeros desea ingresar?: "))
for i in range(pregunta):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    numeros.append(numero)
promedio = calcular_promedio(numeros)
print(f"El promedio de los numeros es: {promedio}")
"""

"""
def contar_mayores(numeros): 
    mayores = 0
    for numero in numeros:
        if numero > 10:
            mayores += 1
    return mayores

numeros = []
pregunta = int(input("¿Cuantos numeros desea ingresar?: "))
for i in range(pregunta):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    numeros.append(numero)
mayores = contar_mayores(numeros)
print(f"El numero de elementos mayores es: {mayores}")
"""

"""
def contar_mayores(numeros): 
    mayores = 0
    for numero in numeros:
        if numero > 10:
            mayores += 1
    return mayores

mayores = contar_mayores([5, 12, 7, 20, 33, 18, 2, 45])
print(f"El numero de elementos mayores es: {mayores}")
"""

"""
def añadir_producto(productos):
    pregunta = int(input("¿Cuantos productos desea agregar?: "))
    for i in range(pregunta):
        nombre_producto = input(f"Ingrese el nombre del producto {i+1}: ")
        if nombre_producto in productos:
            print("El producto ya existe en la lista.")
        else:
            productos.append(nombre_producto)
            print("Producto agregado exitosamente.")

def eliminar_producto(productos):
    print(productos)
    nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
    if nombre_eliminar in productos:
        productos.remove(nombre_eliminar)
        print("Producto eliminado exitosamente.")
    else:
        print("El producto no se encuentra en la lista.")

def mostrar_productos(productos):
    print(productos)
    if len(productos) == 0:
        print("No hay productos en la lista.")

def buscar_producto(productos):
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    for i in range(len(productos)):
        if productos[i] == nombre_buscar:
            print(f"{nombre_buscar} se encuentra en la posicion {i}")
            break
    else:
        print("Producto no encontrado")

productos = []
while True:
    print("====== Menú de opciones ======")
    print("[1] Agregar producto [2] Eliminar producto [3] Mostrar todos [4] Buscar producto [5] Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        añadir_producto(productos)
    elif opcion == "2":
        eliminar_producto(productos)
    elif opcion == "3":
        mostrar_productos(productos)
    elif opcion == "4":
        buscar_producto(productos)
    elif opcion == "5":
        print("Gracias por usar el programa.")
        break
    else:
        print("Opción no válida, intente de nuevo.")
"""

"""
nombre_ventas = []
ventas = []
venta_mayor = 0

for i in range(5):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    ventas_producto = int(input(f"Ingrese la cantidad de ventas del producto {i+1}: "))
    
    nombre_ventas.append(nombre)
    ventas.append(ventas_producto)
    for i in range(len(ventas)):
        if ventas[i] > venta_mayor:
            venta_mayor = ventas[i]
            indice_venta_mayor = i
print(f"El producto con mayor ventas es: {nombre_ventas[indice_venta_mayor]} con {venta_mayor} ventas.")
"""

"""
import random
matriz = []
for i in range(3): 
    fila = []
    for j in range(3):
        numero_aleatorio = random.randint(1, 100)
        fila.append(numero_aleatorio)
    matriz.append(fila)
print("Matriz generada:")
for fila in matriz:
    print(fila)
"""

"""
import random
matriz = []
for i in range(3): 
    fila = []
    for j in range(3):
        numero_aleatorio = random.randint(1, 100)
        fila.append(numero_aleatorio)
    matriz.append(fila)
print("Matriz generada:")
for fila in matriz:
    print(fila, end ='\t')
    print()
    """

"""
notas = []
aprobados = []
reprobados = []
aprobados_notas = 0
reprobados_notas = 0

while True:
    seccion = int(input("Cuantos estudiantes hay en la seccion?: "))
    if seccion <= 0:
        print("Error, no se pueden ingresar numeros menores a 0, intente de nuevo.")
    else:
        for i in range(seccion):
            nota = int(input(f"Ingrese la nota del estudiante {i+1} (1.0 a 7.0): "))
            if nota < 1.0 or nota > 7.0:
                print("Nota invalida, intente de nuevo.")
                nota = int(input(f"Ingrese la nota del estudiante {i+1} (1.0 a 7.0): "))
            notas.append(nota)
            if nota >= 4.0:
                aprobados.append(nota)
                aprobados_notas += 1
            else:
                reprobados.append(nota)
                reprobados_notas += 1
            promedio = sum(notas) / len(notas)
        print(f"El numero de estudiantes aprobados es: {aprobados_notas}")
        print(aprobados)
        print(f"El numero de estudiantes reprobados es: {reprobados_notas}")
        print(reprobados)
        print(f"El promedio de las notas es: {promedio}")
    """


def añadir_producto(productos, precios):
    pregunta = int(input("¿Cuantos productos desea agregar?: "))
    for i in range(pregunta):
        nombre_producto = input(f"Ingrese el nombre del producto {i+1}: ")
        precio_producto = float(input(f"Ingrese el precio del producto {i+1}: "))
        if nombre_producto in productos:
            print("El producto ya existe en la lista.")
        else:
            productos.append(nombre_producto)
            precios.append(precio_producto)
            print("Producto agregado exitosamente.")

def eliminar_producto(productos, precios):
    print(productos)
    nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ")
    if nombre_eliminar in productos:
        indice = productos.index(nombre_eliminar)
        del productos[indice]
        del precios[indice]
        print("Producto eliminado exitosamente.")
    else:
        print("El producto no se encuentra en la lista.")

def mostrar_todos(productos, precios):
    if len(productos) == 0:
        print("No hay productos en las listas.")
    else:
        for i in range(len(productos)):
            print(f"Producto: {productos[i]}, Precio: {precios[i]}")

def buscar_producto(productos, precios):
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    for i in range(len(productos)):
        if productos[i] == nombre_buscar:
            print(f"{nombre_buscar} se encuentra en la posicion {i} con precio {precios[i]}")
            break
    else:
        print("Producto no encontrado")

productos = []
precios = []

while True:
    print("====== Menú de opciones ======")
    print("[1] Agregar producto y precio [2] Eliminar producto [3] Mostrar todos [4] Buscar producto [5] Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        añadir_producto(productos, precios)
    elif opcion == 2:
        eliminar_producto(productos, precios)
    elif opcion == 3:
        mostrar_todos(productos, precios)
    elif opcion == 4:
        buscar_producto(productos, precios)
    elif opcion == 5:
        print("Gracias por usar el programa.")
        valor_total_inventario = sum(precios)
        print(f"El valor total del inventario es: {valor_total_inventario}")
        break