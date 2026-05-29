"""
import random
dado = random.randint(1, 6)
print("El numero del dado es:", dado)

import random
suerte = random.random()
# da por ej:  0.7423349...
if suerte < 0.3:
    print(suerte)
    print("¡Te ganaste un descuento!")
else:
    print(suerte)
    print("Sigue intentando")
"""
"""
while True:
    print("==== Menú ====")
    print("[1] Saludar [2] Despedirse [3] Salir")
    
    opcion = input("Elija: ")

    if opcion == "1":
        print("Hola")
    elif opcion == "2":
        print("Adios")
    elif opcion == "3":
        print("Fin")
        break
    else:
        print("Opción no válida.")
"""
"""
while True:
    print("[1] Saludar [2] Despedirse [3] Salir")
    opcion = input("Elija una opcion: ")

    if not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        print("Opcion no valida intente nuevamente.")
        continue

    if opcion == "1": 
        print("Hola")
    elif opcion == "2": 
        print("Adios")
    else: 
        print("Fin")
        break
"""
"""
while True:
    print("[1] Vender")
    print("[2] Total")
    print("[3] Salir")
    op = input("Elija: ")
    
    if op == "1":
        print("ventas")
    elif op == "2":
        print("Total")
    elif op == "3":
        print("salir")
        break
"""
"""
def mostrar_menu():
    print("[1] Saludar [2] Despedirse [3] Salir")

def vender():
    print("Vendido")

def total():
    print("Total")

while True:
    mostrar_menu()
    op = input("Elija: ")
    if op == "1":
        vender()
    elif op == "2":
        total()
    elif op == "3":
        break
"""

"""
lista_producto = []
while True:
    print("==== Lista de inventario ====")
    print("[1] Agregar producto [2] Eliminar producto [3] Mostrar todos [4] Buscar producto [5] Salir")

    opcion = input("Elija una de las opciones: ")

    if opcion == "1":
        producto = input("Escriba el producto a agregar: ")
        lista_producto.append(producto)
        print("Producto añadido")
    elif opcion == "2":
        print(lista_producto)
        eliminar = input("Elija el producto a eliminar: ")
        if lista_producto:
            print("\nLa lista no esta vacia, puede proceder")
            lista_producto.remove(eliminar)
            print("\nProducto eliminado")
        else:
            print("La lista esta vacia debe agregar productos primero")
    elif opcion == "3":
        print("Mostrando lista")
        print(lista_producto)
    elif opcion == "4":
        busqueda = input("¿Que elemento deseas buscar?: ")
        if busqueda in lista_producto:
            print("El producto esta")
            print("posicion del producto", lista_producto.index(busqueda))
        else:
            pregunta = ("El elemento no esta en la lista desea agregarla? (s/n): ")
            if pregunta == "s":
                lista_producto.append(busqueda)
                print("Producto agregado")
            elif pregunta == "n":
                print("Producto no agregado")
    elif opcion == "5":
        print("Saliendo")
        break
"""
"""
nombres = []
asistencia = []
n = int(input("Cuantos estudiantes desea ingresar?: "))
for i in range(n):
    alumno = input(f"Ingrese el nombre del {i+1} alumno: ")
    nombres.append(alumno)
    asistencias = int(input(f"Ingrese cuantas asistencia tiene el {i+1} alumno: "))
    asistencia.append(asistencias)
total_asistencias = sum(asistencia)
promedio_total = total_asistencias / n
asistencia_maxima = max(asistencia)
indice_maximo = asistencia.index(asistencia_maxima)
estudiante_maximo = nombres[indice_maximo]
print(f"El alumno con mayor asistencias es {estudiante_maximo} con {asistencia_maxima} asistencias")
print("EL promedio de asistencias es: ", promedio_total)
print("El total de asistencias es: ", total_asistencias)
print("Listas de estudiantes: ", nombres) 
print("Asistencias de estudiantes: ", asistencia)
"""

sucursales = []
ventas = []
pregunta = int(input("¿Cuantas sucursales va a registrar?: "))
for i in range(pregunta):
    nombre_sucursal = input(f"Ingrese el nombre de la {i+1} sucursal: ")
    sucursales.append(nombre_sucursal)
    ventas_sucursal = int(input(f"Ingrese el total de ventas de la {i+1} sucursal: "))
    ventas.append(ventas_sucursal)
ventas_total = sum(ventas)
promedio_ventas = ventas_total / pregunta
venta_mayor = max(ventas)
indice_venta_mayor = ventas.index(venta_mayor)
sucursal_mayor = sucursales[indice_venta_mayor]
venta_menor = min(ventas)
indice_venta_menor = ventas.index(venta_menor)
sucursal_menor = sucursales[indice_venta_menor]
print(f"La sucursal con mayores ventas es {sucursal_mayor} con {venta_mayor} ventas")
print(f"La sucursal con mayores ventas es {sucursal_menor} con {venta_menor} ventas")
print("El promedio de ventas es:", promedio_ventas)
print("El total de ventas es: ", ventas_total)
print("Lista de sucursales: ", sucursales)
print("lista de ventas: ", ventas)



