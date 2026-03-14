#Ejercicio 1
#Rut = input("Ingrese su rut personal(con puntos y guion): ")
#Nombre = input("Ingrese su nombre y apellido: ")
#Direccion = input("Ingrese su direccion de casa: ")
#Correo = input("Ingrese su correo personal: ")

#print("\nDatos personales: ")
#print("Rut:", Rut)
#print("Nombre:", Nombre)
#print("Direccion:", Direccion)
#print("Correo:", Correo)


#Ejercicio 2
#num1 = int(input("Ingrese el primer número: "))
#num2 = int(input("Ingrese el segundo número:"))

#suma = num1 + num2
#resta = num1 - num2
#multiplicacion = num1 * num2 
#division = num1 / num2 

#print("\nResultados: ")
#print("Suma:", suma)
#print("Resta:", resta)
#print("Multiplicación:", multiplicacion)
#print("División:", division)


#Ejercicio 3
#Caso 1
voltaje = float(input("Ingrese el voltaje en voltios: "))
resistencia = float(input("Ingrese la resistencia en ohmios: "))

corriente = voltaje / resistencia

print("\nResultados: ")
print("Voltaje: ", voltaje, "V")
print("Resistencia: ", resistencia, "Ω")
print("Corriente: ", corriente, "A")


#Caso 2
voltaje = float(input("Ingrese el voltaje en voltios: "))
corriente = float(input("Ingrese la corriente en amperios: "))

resistencia = voltaje / corriente

print("\nResultados: ")
print("Voltaje: ", voltaje, "V")
print("Corriente: ", corriente, "A")
print("Resistencia: ", resistencia, "Ω")


#Caso 3
corriente = float(input("Ingrese la corriente en amperios: "))
resistencia = float(input("Ingrese la resistencia en ohmios: "))

voltaje = corriente * resistencia

print("\nResultados: ")
print("Voltaje: ", voltaje, "V")
print("Corriente: ", corriente, "A")
print("Resistencia: ", resistencia, "Ω")



# Ejercicio 4
precio = float(input("Ingrese el precio del producto: "))
viajes = int(input("Ingrese la cantidad de viajes realizados: "))
gasto_total = int(input("Ingrese el gasto total en transporte: "))

gasto_dia = precio * viajes
dias = 10000 // gasto_dia 

print("\nResultados: ")
print("Precio de transporte: ", precio)
print("Viajes realizados: ", viajes)
print("Gasto total hoy: ", gasto_dia)
print("Días que alcanza 10.000: ", dias)


#Ejercicio 5
cuenta_total = float(input("Ingrese el total de la cuenta: "))
porcentaje = float(input("Ingrese el porcentaje de la propina: "))

propina = cuenta_total * (porcentaje / 100)
total_final = cuenta_total + propina

print("\nResultados: ")
print("Total de la cuenta: ", cuenta_total)
print("Propina: ", porcentaje)
print("Monto de la propina: ", propina)
print("Total a pagar: ", total_final)


#Ejercicio 6
peso = float(input("Ingrese su peso en kg: "))

gramos = peso * 1000
libras = peso * 2.20462
onzas = peso * 35.274

print("\nResultados: ")
print("Peso en kilogramos: ", peso)
print("Peso en gramos: ", gramos)
print("Peso en libras: ", libras)
print("Peso en onzas: ", onzas)


#Ejercicio 7
distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
tiempo = float(input("Ingrese el tiempo empleado en horas: "))

velocidad = distancia / tiempo 
minutos = tiempo * 60 

print("\nResultados: ")
print("Distancia (km): ", distancia)
print("Tiempo (horas): ", tiempo)
print("Velocidad: ", velocidad, "km/h")
print("Tiempo en minutos: ", minutos, "minutos")