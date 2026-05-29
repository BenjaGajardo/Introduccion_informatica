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
"""
"""
def crear_estudiante(usuario):
    for clave in usuario:
        nuevo_valor = input(f"Ingrese el valor para '{clave}': ")
        usuario[clave] = nuevo_valor
    
usuario = {"nombre": "", "edad": "", "carrera": ""}

print("Por favor, completa la siguiente información:")
crear_estudiante(usuario)

print("\nDatos actualizados:", usuario)
"""



