ventas_semana = 7
total_ventas = 0
i = 1
mayor_venta = 0
while i <= ventas_semana:
    while True:
        monto_dia = int(input(f"Monto del día {i}: "))
        if monto_dia >= 0:
            break
        else:
            print("Error: el monto no puede ser negativo.")
    total_ventas += monto_dia
    if monto_dia > mayor_venta:
        mayor_venta = monto_dia
    i += 1
promedio_ventas = total_ventas / ventas_semana
if total_ventas > 100000:
    print("\n¡Cuota superada! Felicidades")
else:
    print("\nCuota no alcanzada. Sigue esforzándote.")
print("\nResumen de ventas:")
print("Total de ventas de la semana:", total_ventas)
print("Promedio de ventas diarias:", promedio_ventas)
print("Mayor venta realizada en la semana:", mayor_venta)


ventas_productos = 5
i = 1
total_ventas = 0
mayor_venta = 0
while i <= ventas_productos:
    while True:
        monto_venta = int(input(f"Monto de la venta {i}: "))
        if monto_venta >= 0:
            break
        else:
            print("Error el monto no puede ser negativo.")
    total_ventas += monto_venta
    if monto_venta > mayor_venta:
        mayor_venta = monto_venta
    i += 1
    promedio_ventas = total_ventas / ventas_productos
if total_ventas > 100000:
    print("\n¡Cuota superada! Felicidades")
else:
    print("\ncuota no alcanzada. Sigue esforzándote")
print("\nResumen de ventas:")
print("Total de ventas de la semana:", total_ventas)
print("Promedio de ventas diarias:", promedio_ventas)
print("Venta mayor realizada en la semana:", mayor_venta)


conteo = 0
i = 1
conteo_usuario = int(input("Ingrese el conteo(presione 0 para salir): "))
while i <= conteo:
    while True:
        conteo = int(input(f"Ingrese el conteo{i}(presione 0 para salir):"))
        if conteo >= 0:
            break
        else:
            conteo += 1
    i += 1
    suma_conteos = conteo + conteo_usuario
    conteos_positivo = suma_conteos
    conteos_negativo = suma_conteos - conteo
    print("Total de conteos:", conteos_positivo)
    print("Total de conteos:", conteo)
    print("Total de conteos:", conteo_usuario)
    print("Total de conteos:", conteos_negativo)


paneles = int(input("¿Cuantos paneles desea registrar?: "))
if paneles <= 0:
    print("Error, debe ingresar un numero valido")
    paneles = int(input("Ingrese nuevamente el numero de paneles: "))
i = 1
panel_total = 0
panel_alto = 0
while i <= paneles:
    while True:
        panel = int(input(f"Ingrese el voltaje del panel {i}: "))
        if panel >= 0:
            break
        else:
            print("Error: el panel no puede ser negativo.")
    i += 1
    suma_panel = panel + panel
    if panel_alto < panel:
        panel_alto = panel
    panel_total = panel_total + panel
    panel_promedio = panel_total / paneles
if panel_total > 24:
    print("¡Alerta voltaje sobre el estandar!")
else:
    print("Voltaje en modo ahorro")
print("\nResumen de paneles:")
print("Total de paneles:", panel_total)
print("Promedio de paneles:", panel_promedio)
print("Panel mas alto:", panel_alto)



numero = int(input("Ingrese un numero: "))

while numero <= 0:

    print("El numero no debe ser 0 ")

    numero = int(input("Ingrese un numero: "))

for i in range(numero):

    print("Hola")




suma_notas = 0

pregunta = int(input("¿Cuantas notas desea promediar?: "))

while pregunta <= 0:

    print("Error debe al menos una nota")

    pregunta = int(input("¿Cuantas notas desea promediar?: "))

for i in range(pregunta):

    nota = int(input("Ingrese la nota: "))

    suma_notas = suma_notas + nota

promedio = suma_notas / pregunta

print("El promedio es: ", promedio)


suma_notas = 0
pregunta = int(input("¿Cuantas notas desea promediar?: "))
while pregunta <= 0:
    print("Error debe al menos una nota")
    pregunta = int(input("¿Cuantas notas desea promediar?: "))
for i in range(pregunta):
    nota = int(input("Ingrese la nota: "))
    suma_notas = suma_notas + pregunta
promedio = suma_notas / nota
print("El promedio es: ", promedio)


pregunta = int(input("¿Cuantos Paneles tiene el sistema?: "))
while pregunta <= 0:
    print("Error el numero no debe ser ni negativo ni cero")
    pregunta = int(input("¿Cuantos Paneles tiene el sistema?: "))
total_voltaje = 0
voltaje_maximo = 0
for i in range(pregunta):
    panel = int(input(f"Ingrese el voltaje del panel{i+1}: "))
    total_voltaje = total_voltaje + panel
    if voltaje_maximo < panel:
        voltaje_maximo = panel
promedio = total_voltaje / pregunta
print("El promedio es", promedio)
print("El voltaje maximo es", voltaje_maximo)



pregunta = int(input("¿cuantas ventas realizaste hoy?: "))
while pregunta <= 0:
    print("Error el numero no debe ser negativo ni cero")
    pregunta = int(input("¿Cuantas ventas realizaste hoy?: "))
suma_ventas = 0
venta_mayor = 0
for i in range(pregunta):
    venta = int(input(f"Ingrese el valor{i+1}: "))
    if venta > 50000:
        print("¡Venta excelente!")
    if venta_mayor < venta:
        venta_mayor = venta
    suma_ventas = suma_ventas + venta
promedio_ventas = suma_ventas / pregunta 
if suma_ventas > 100000:
    print("\nMeta del dia alcanzada")
else:
    print("\nMeta no alcanzada")
print("El promedio es", promedio_ventas)
print("La venta mayor es", venta_mayor)



contador = 0
promedio_nivel = 0
nivel_alto = 0
suma_nivel = 0
pregunta = int(input("¿Cuantas personas intentara ingresar hoy?: "))
while pregunta <= 0:
    print("Error el numero debe ser mayor a 0")
    pregunta = int(input("¿Cuantas personas intentara ingresar hoy?: "))
for i in range(pregunta):
    nivel = int(input(f"Ingrese el nivel de acceso (entre un numero del 1 al 7) de la persona {i+1}: "))
    if nivel >= 7:
        print("Acceso concedido a area restringida")
    else:
        print("Acceso denegado, nivel insuficiente")
        contador += 1
    if nivel_alto < nivel:
        nivel_alto = nivel
    suma_nivel = suma_nivel + nivel
promedio = suma_nivel / pregunta
if contador >= 3:
    print("\nAlerta de seguridad: Demaciados intentos fallidos")
else:
    print("\nTodo normal")
print("\nLista de respuestas final")
print("Promedio del nivel de acceso: ", promedio)
print("Nivel de acceso mas alto: ", nivel_alto)
print("Total de personas rechazadas: ", contador)




