#edad = int(input("Ingrese su edad: "))
#if edad >= 18:
#    print("Usted es mayor de edad.")
#else:
#    print("Usted es menor de edad.")


#numero = int(input("Ingrese un número: "))
#if numero % 2 == 0:
#    print("El numero es par.")
#else:
#    print("El numero es impar.")


#temperatura = int(input("Ingrese la temperatura en grados celsius: "))
#if temperatura >= 25:
#    print("Hace calor.")
#elif temperatura >= 15:
#    print("La temperatura es agradable.")
#else:
#    print("Hace frío.")


año = int(input("Ingrese su año de nacimiento: "))
edad = 2026 - año
if edad >= 18:
    print("Usted puede conducir.")
    pregunta= input("¿Usted bebe alcohol? (si/no): ")
    if pregunta == "si":
        print("Si bebe pasa la llave a un amigo que no tome")
    else:
        print("¡Lo felicito!")
else:
    pregunta2 = input("En que curso estas?: ")
    pregunta3 = input("¿Que quieres ser profesionalmente?: ")
    print("¡Suerte con tu carrera de", pregunta3, "en el curso de", pregunta2, "!")