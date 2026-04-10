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