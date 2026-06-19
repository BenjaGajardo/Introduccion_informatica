"""
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        print(f"Libro:", self.titulo,  "Autor:", self.autor,  "Páginas:", self.paginas)

    def es_corto(self):
        if self.paginas < 100:
            return True
        else:
            return False

libro_corto = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
libro_largo = Libro("Cien años de soledad", "Gabriel García Márquez", 496)

libro_corto.mostrar_info()
print(f"¿Es corto?: {libro_corto.es_corto()}")
libro_largo.mostrar_info()
print(f"¿Es corto?: {libro_largo.es_corto()}")
"""

"""
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

mi_rectangulo = Rectangulo(5, 3)
print(f"Área del rectángulo: {mi_rectangulo.area()}")
print(f"Perímetro del rectángulo: {mi_rectangulo.perimetro()}")
"""

"""
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

mi_cuadrado = Cuadrado(4)
print(f"Área del cuadrado: {mi_cuadrado.area()}")
print(f"Perímetro del cuadrado: {mi_cuadrado.perimetro()}")
"""

"""
class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.pi = 3.1416

    def area(self):
        return self.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * self.pi * self.radio

mi_circulo = Circulo(2)
print(f"Área del círculo: {mi_circulo.area()}")
print(f"Perímetro del círculo: {mi_circulo.perimetro()}")
"""

"""
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

triangulo1 = Triangulo(6, 4)
triangulo2 = Triangulo(10, 5)
print(f"Área del Triángulo 1: {triangulo1.area()}")
print(f"Área del Triángulo 2: {triangulo2.area()}")
"""

"""
class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def mostrar_info(self):
        print(f"Canción:", self.titulo, "-",  "Artista:", self.artista)

    def duracion_en_minutos(self):
        return self.duracion / 60

mi_cancion = Cancion("Moscow Mule", "Bad bunny", 200)
mi_cancion.mostrar_info()
print(f"Duración: {mi_cancion.duracion_en_minutos()} minutos")
"""

"""
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        return self.precio * self.cantidad

    def aplicar_descuento(self, porcentaje):
        self.precio = self.precio - (self.precio * porcentaje / 100)
        print(f"¡Se aplicó un descuento del {porcentaje}%!")

laptop = Producto("Laptop", 800, 3)
print(f"Valor total inicial: ${laptop.valor_total()}")
laptop.aplicar_descuento(10)
print(f"Nuevo valor total (con descuento): ${laptop.valor_total()}")
"""

"""
class Temperatura:
    def __init__(self, grados_celsius):
        self.grados_celsius = grados_celsius

    def a_fahrenheit(self):
        return (self.grados_celsius * 9 / 5) + 32

    def a_kelvin(self):
        return self.grados_celsius + 273.15

temp = Temperatura(25)
print(f"Temperatura: {temp.grados_celsius}°C")
print(f"En Fahrenheit: {temp.a_fahrenheit()}°F")
print(f"En Kelvin: {temp.a_kelvin()}K")
"""

"""
class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base

    def sueldo_con_bono(self, bono):
        return self.sueldo_base + bono

    def aumentar_sueldo(self, porcentaje):
        self.sueldo_base = self.sueldo_base + (self.sueldo_base * porcentaje / 100)
        print(f"Sueldo base aumentado en un {porcentaje}% permanentemente.")

empleado1 = Empleado("Ana", 2000)
print(f"Sueldo base de {empleado1.nombre}: ${empleado1.sueldo_base}")
print(f"Sueldo con bono de $300: ${empleado1.sueldo_con_bono(300)}")
print(f"Sueldo base sigue siendo: ${empleado1.sueldo_base}")
empleado1.aumentar_sueldo(15)
print(f"Nuevo sueldo base permanente: ${empleado1.sueldo_base}")
"""