"""
def nombre_del_procedimiento():
# Instrucciones
# que se ejecutarán
    print('Algo')
# Para llamarlo:
nombre_del_procedimiento()

def saludar():
    print('¡Hola, bienvenido!')
    print('Esperamos que tengas')
    print('una excelente sesión.')
# Llamamos al procedimiento
saludar()
# Lo podemos llamar otra vez
saludar()


def saludar(nombre):
    print(f'¡Hola, {nombre}!')
    print('Bienvenido al sistema')
# Tres llamadas, tres saludos personalizados
saludar('María')
saludar('Juan')
saludar('Sofía')


def mostrar_area_circulo(radio):
    PI = 3.1416
    area = PI * radio * radio
    print(f'El área del círculo es: {area}')
# Llamadas con distintos radios
mostrar_area_circulo(5)
mostrar_area_circulo(10)
mostrar_area_circulo(2.5)


def doble(x):
    return x * 2 # entrega el resultado
    print('hola') # esto NUNCA se ejecuta
resultado = doble(5) # resultado guarda 10


def sumar(a, b):
    resultado = a + b
    return resultado
# Forma 1: guardar en variable y usarla
x = sumar(3, 5)
print(x) # imprime 8
# Forma 2: usar directamente en otra expresión
print(sumar(10, 20)) # imprime 30
# Forma 3: combinar con otros cálculos
total = sumar(5, 2) * 10
print(total) # imprime 70


def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def operacion_mixta(x, y):
    s = sumar(x, y) # llamamos a sumar
    r = restar(x, y) # llamamos a restar
    return s * r # devolvemos el producto
# (10+3) * (10-3) = 91
print(operacion_mixta(10, 3))


def calcular_imc(peso, altura):
    return peso / (altura * altura)
def clasificar_imc(imc):
    if imc < 18.5:
        return 'Bajo peso'
    elif imc < 24.9:
        return 'Peso normal'
    elif imc < 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidad'
peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = calcular_imc(peso, altura)
estado = clasificar_imc(imc)
print(f'Tu IMC es {imc:.2f} ({estado})')


def doblar(num):
    return num * 2
doblar = lambda num: num * 2
print(doblar)


def pedir_notas():
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    return nota1, nota2, nota3

def calcular_promedio(notas):
    sumas = sum(notas)
    promedio = sumas / len(notas)
    return promedio

def clasificar_promedio(promedio):
    if promedio <= 4.0: 
        return "Reprobado"
    else: 
        return "Aprobado"

def mostrar_reporte(notas, promedio, estado):
    print(f"las notas fueron {notas}")
    print(f"el promedio de las notas es {promedio:.2f}")
    print(f"el estado del promedio es {estado}")

notas = pedir_notas()
promedio = calcular_promedio(notas)
estado = clasificar_promedio(promedio)
mostrar_reporte(notas, promedio, estado)


def numero_despues(n):
    suma = n + 1
    return suma

n = int(input("Ingrese un numero: "))
print(numero_despues(n))


def contar_caracteres(texto):
    total = len(texto)
    return total

texto = input("Ingrese un texto: ")
print(contar_caracteres(texto))

"""

"""
def numeros1(n):
    elevado = n ** 2
    return elevado
n = int(input("Ingrese un numero: "))
print(numeros1(n))
pregunta = input("desea ingresar otro numero? (s/n): ")
while pregunta != "n":
    def numeros1(n):
        elevado = n ** 2
        return elevado
    n = int(input("Ingrese un numero: "))
    print(numeros1(n))
    pregunta = input("desea ingresar otro numero? (s/n): ")
else:
    print("Fin del procedimiento")
"""

"""
def numeros_comparacion(n):
    if n < 20:
        return "El numero es menor"
    elif n > 20:
        return "El numero es mayor"
    else:
        return "El numero es igual"
n = int(input("Ingrese un numero: "))
print(numeros_comparacion(n))
pregunta = input("Desea ingresar otro numero? (s/n): ")
while pregunta != "n":
    def numeros_comparacion(n):
        if n < 20:
            return "El numero es menor"
        elif n > 20:
            return "El numero es mayor"
        else:
            return "El numero es igual"
    n = int(input("Ingrese un numero: "))
    print(numeros_comparacion(n))
    pregunta = input("Desea ingresar otro numero? (s/n): ")
else: 
    print("Fin del procedimiento")


def crear_estudiante(usuario):
    for clave in usuario:
        nuevo_valor = input(f"Ingrese el valor para '{clave}': ")
        usuario[clave] = nuevo_valor
    
usuario = {"nombre": "", "edad": "", "carrera": ""}

print("Por favor, completa la siguiente información:")
crear_estudiante(usuario)

print("\nDatos actualizados:", usuario)
"""

"""
def pedir_notas():
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    return nota1, nota2, nota3

def calcular_promedio(notas):
    sumas = sum(notas)
    promedio = sumas / len(notas)
    return promedio

def clasificar_promedio(promedio):
    if promedio <= 4.0: 
        return "Reprobado"
    else: 
        return "Aprobado"

def mostrar_reporte(notas, promedio, estado):
    print(f"las notas fueron {notas}")
    print(f"el promedio de las notas es {promedio:.2f}")
    print(f"el estado del promedio es {estado}")

notas = pedir_notas()
promedio = calcular_promedio(notas)
estado = clasificar_promedio(promedio)
mostrar_reporte(notas, promedio, estado)
"""

"""
def leer_entero_en_rango(mensaje, minimo, maximo):
    while True:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            return numero
        else:
            print(f"Error: el numero debe estar entre {minimo} y {maximo}.")    
edad = leer_entero_en_rango("Ingrese su edad: ", 0, 120)
print(f"Su edad es: {edad}")
nota = leer_entero_en_rango("Ingrese su nota: ", 0, 100)
print(f"Su nota es: {nota}")
"""

"""
def agregar_contacto(contactos):
    pregunta = int(input("Cuantos contactos desea agregar?: "))
    for i in range(pregunta):
        nombre_contacto = input(f"Ingrese el nombre del contacto {i+1}: ")
        telefono_contacto = input(f"Ingrese el numero de telefono del contacto {i+1}: ")
        contactos[nombre_contacto] = telefono_contacto
    return contactos

def buscar_telefono(contactos):
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
    if nombre_buscar in contactos:
        print(f"El numero de telefono de {nombre_buscar} es: {contactos[nombre_buscar]}")
    else:
            print(f"El contacto {nombre_buscar} no se encuentra en la agenda.")

def actualizar_telefono(contactos):
    print(contactos)
    pregunta2 = int(input("Cuantos contactos desea actualizar?: "))
    for i in range(pregunta2):
        nombre_actualizar = input(f"Ingrese el nombre del contacto {i+1} a actualizar: ")
        if nombre_actualizar in contactos:
            nuevo_telefono = input(f"Ingrese el nuevo numero de telefono para {nombre_actualizar}: ")
            contactos[nombre_actualizar] = nuevo_telefono
            print(f"El numero de telefono de {nombre_actualizar} ha sido actualizado a: {nuevo_telefono}")
        else:
            print(f"El contacto {nombre_actualizar} no se encuentra en la agenda.")


def eliminar_contactos(contactos):
    print(contactos)
    pregunta3 = int(input("Cuantos contactos desea eliminar?: "))
    for i in range(pregunta3):
        nombre_eliminar = input(f"Ingrese el nombre del contacto {i+1} a eliminar: ")
        if nombre_eliminar in contactos:
            contactos.pop(nombre_eliminar)
            print(f"El contacto {nombre_eliminar} ha sido eliminado.")
        else:
            print(f"El contacto {nombre_eliminar} no se encuentra en la agenda.")

contactos = {}

while True:
    print("===== Agenda =====")
    print("[1] agregar contacto [2] Buscar telefono por nombre [3] actualizar telefono [4] Eliminar contacto [5] Salir")
    eleccion = int(input("Ingrese su eleccion: "))
    if eleccion == 1:
        contactos = agregar_contacto(contactos)
        print("\n===== Contactos Agregados =====")
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")
    elif eleccion == 2:
        buscar_telefono(contactos)
    elif eleccion == 3:
        actualizar_telefono(contactos)
    elif eleccion == 4:
        eliminar_contactos(contactos)
    elif eleccion == 5:
        print("Saliendo del menu...")
        break
    """


"""
grados = int(input("Ingrese los grados que desea transformar: "))

def convercion_grados(grados):
    f = (grados * 1.8) + 32
    return "grados fahrenheit transformados", f

print(convercion_grados(grados))
"""
"""
def crear_producto(nombre, precio, stock):
    return {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
        }

def mostrar_producto(crear_producto):
    print("Producto: ", crear_producto["nombre"])
    print("Precio: $", crear_producto["precio"],"unidades")
    print("Stock: ", crear_producto["stock"])


nombre = input("Ingrese el nombre del producto: ")
precio = int(input("Ingrese el precio del producto: "))
stock = int(input("Ingrese el stock del producto: "))
producto_list = []

producto = crear_producto(nombre, precio, stock)
mostrar_producto(producto)
producto_list.append(producto)
print(producto_list)
"""

"""
def agregar_productos(inventario):
    pregunta1 = int(input("Cuantos productos desea agregar?: "))
    for i in range(pregunta1):
        nombre_producto = input(f"Ingrese el nombre del producto {i+1}: ")
        inventario[nombre_producto] = 0
        valor = int(input(f"Ingrese el valor del producto {i+1}: "))
        inventario[nombre_producto] = valor
        stock = int(input(f"Ingrese el stock del producto {i+1}: "))
        inventario[nombre_producto] = stock
        print(f"El producto {nombre_producto} ha sido agregado al inventario.")
    return inventario

def registrar_venta(inventario):
    print(inventario)
    pregunta2 = int(input("Cuantos productos desea registrar?: "))
    for i in range(pregunta2):
        nombre_producto = input(f"Ingrese el nombre del producto {i+1}: ")
        if nombre_producto in inventario:
            cantidad = int(input("Ingrese la cantidad vendida: "))
            ventas = inventario[nombre_producto] - cantidad
            print(f"El producto {nombre_producto} ha sido vendido.")
            inventario[nombre_producto] = ventas
        else:
            print(f"El producto {nombre_producto} no se encuentra en el inventario.")

def mostrar_inventario(inventario):
    print(inventario)

def mostrar_resumen(inventario):
    total = 0
    for producto in inventario:
        total += inventario[producto]
    print(f"El total de productos vendidos es: {total}")
    total_recaudado = 0
    for producto in inventario:
        total_recaudado += inventario[producto] * inventario[producto]
    print(f"El total recaudado es: {total_recaudado}")

inventario = {}

while True:
    print("menu de inventario")
    print("[1] Agregar producto nuevo [2] Registrar venta [3] Mostrar inventario [4] Mostrar resumen del dia [5] Salir")
    opcion = int(input("Elija una de las opciones: "))
    if opcion == 1:
        inventario = agregar_productos(inventario)
    elif opcion == 2:
        registrar_venta(inventario)
    elif opcion == 3:
        mostrar_inventario(inventario)
    elif opcion == 4:
        mostrar_resumen(inventario)
    elif opcion == 5:
        print("Saliendo del menu...")
        break
"""

