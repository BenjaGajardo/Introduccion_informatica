"""
productos = {"leche": 2500, "queque": 1500, "polenta": 3000, "puerro": 5000, "manzana": 1000}
print("===== Lista de productos =====")
for producto, precio in productos.items():
    print(f"{producto}: ${precio}")
monto_total = sum(productos.values())
print(f"El monto total de los productos es: ${monto_total}")
producto_barato = min(productos.values())
print(f"El producto más barato es: ${producto_barato}")
producto_caro = max(productos.values())
print(f"El producto mas caro es: ${producto_caro}")
"""

"""
def agregar_contacto(nombre_telefono):
    pregunta = int(input("¿Cuantos usuarios desea agregar?: "))
    for i in range(pregunta):
            nombre_tel = input(f"Ingrese el nombre del contacto {i+1}: ")
            telefono = int(input(f"Ingrese el numero de telefono {i+1}: "))
            nombre_telefono[nombre_tel] = telefono
            print("Contacto agregado exitosamente.")
    return nombre_telefono

def buscar_telefono(nombre_telefono):
    pregunta = int(input("¿Cuantos usuarios desea buscar?: "))
    for i in range(pregunta):
        nombre = input(f"Ingrese el nombre del contacto {i+1} que desea buscar: ")
        if nombre in nombre_telefono:
            print(f"El telefono de {nombre} es: {nombre_telefono[nombre]}")
        else:
            print("Contacto no encontrado.")

def actualizar_contacto(nombre_telefono):
    pregunta = int(input("¿Cuantos usuarios desea actualizar?: "))
    for i in range(pregunta):
        nombre_actualizar = input(f"Ingrese el nombre del contacto {i+1} que desea actualizar: ")
        if nombre_actualizar in nombre_telefono:
            nuevo_telefono = int(input(f"Ingrese el nuevo numero de telefono para {nombre_actualizar}: "))
            nombre_telefono[nombre_actualizar] = nuevo_telefono
            print("Contacto actualizado exitosamente.")
        else:
            print("Contacto no encontrado.")

def eliminar_contacto(nombre_telefono):
    pregunta = int(input("¿Cuantos usuarios desea eliminar?: "))
    for i in range(pregunta):
        nombre_eliminar = input(f"Ingrese el nombre del contacto {i+1} que desea eliminar: ")
        if nombre_eliminar in nombre_telefono:
            del nombre_telefono[nombre_eliminar]
            print("Contacto eliminado exitosamente.")
        else:
            print("Contacto no encontrado.")

nombre_telefono = {}
while True:
    print("===== Menu de agenda =====")
    print("[1] Agregar contacto [2] Buscar telefono por nombre [3] actualizar contacto [4] Eliminar contactos [5] Salir")
    opcion = input("ingrese una opcion: ")
    if opcion < "1" or opcion > "5":
        print("Opcion no valida, intente de nuevo.")
    elif opcion == "1":
        agregar_contacto(nombre_telefono)
    elif opcion == "2":
        buscar_telefono(nombre_telefono)
    elif opcion == "3":
        actualizar_contacto(nombre_telefono)
    elif opcion == "4":
        eliminar_contacto(nombre_telefono)
    elif opcion == "5":
        print("Gracias por usar la agenda hasta luego.")
        break
    """

"""
def agregar_contacto(notas_estudiantes):
    pregunta = int(input("¿Cuantos estudiantes desea agregar?: "))
    for i in range(pregunta):
            nombre_est = input(f"Ingrese el nombre del estudiante {i+1}: ")
            preguntar_nota = int(input(f"¿Cuantas notas desea agregar para {nombre_est}?: "))
            for i in range(preguntar_nota): 
                nota_est = int(input(f"Ingrese la nota {i+1} para {nombre_est}: "))
                notas_estudiantes[nombre_est] = nota_est
                print("Nota agregada exitosamente.")
    print("Estudiante/es agregado exitosamente.")
    return notas_estudiantes

def agregar_nota(notas_estudiantes):
    pregunta = int(input("¿Cuantos estudiantes desea actualizar?: "))
    for i in range(pregunta):
        nombre_agregar = input(f"Ingrese el nombre del estudiante {i+1} que desea agregar una nota: ")
        if nombre_agregar in notas_estudiantes:
            nueva_nota = int(input(f"Ingrese la nueva nota para {nombre_agregar}: "))
            notas_estudiantes[nombre_agregar] = nueva_nota
            print("Nota agregada exitosamente.")
        else:
            print("Estudiante no encontrado.")

def mostrar_promedios(notas_estudiantes):
    for estudiante, nota in notas_estudiantes.items():
        print(f"El promedio de {estudiante} es: {nota}")

notas_estudiantes = {}
while True:
    print("===== Menu de agenda =====")
    print("1) agregar un estudiante nuevo con sus notas, 2) agregar una nota más a un estudiante existente, 3) mostrar el promedio de cada estudiante, 4 salir.")
    opcion = input("ingrese una opcion: ")
    if opcion < "1" or opcion > "5":
        print("Opcion no valida, intente de nuevo.")
    elif opcion == "1":
        agregar_contacto(notas_estudiantes)
    elif opcion == "2":
        agregar_nota(notas_estudiantes)
    elif opcion == "3":
        mostrar_promedios(notas_estudiantes)
    elif opcion == "4":
        print("Gracias por usar la agenda hasta luego.")
        break
    """

nombres_empleados = []
ventas_del_dia = []

pregunta = int(input("¿Cuantos empleados desea agregar?: "))
for i in range(pregunta):
    nombre_empleado = input(f"Ingrese el nombre del empleado {i+1}: ")
    nombres_empleados.append(nombre_empleado)
    ventas_empleado = int(input(f"Ingrese las ventas del empleado {i+1}: "))
    ventas_del_dia.append(ventas_empleado)
ventas_empleados = dict(zip(nombres_empleados, ventas_del_dia))
print("Diccionario de empleados y ventas: ", ventas_empleados)
total_ventas = sum(ventas_empleados.values())
print(f"El total de ventas del día es: {total_ventas}")
mayor_venta = max(ventas_empleados.values())
print(f"La mayor venta del dia es: {mayor_venta}")
menor_venta = min(ventas_empleados.values())
print(f"La menor venta del dia es: {menor_venta}")