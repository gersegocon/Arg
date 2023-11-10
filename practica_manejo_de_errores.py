
"""Practica_Manejo_de_errores.ipynb
---
# ***Argentina Programa 4.0 - Programación Avanzada con Python***
---

## **Módulo 2**: Validación de Datos -  Práctica

### ***Universidad Nacional de Chilecito***

---

# Problemas

* Escribe un programa que le pida al usuario ingresar un número y valide que el valor ingresado sea de tipo numérico. Si el valor no es numérico, el programa debe solicitar al usuario que ingrese un valor válido.
"""

numero = input("Ingrese un número: ")
while not (numero.replace(".", "", 1).isdigit()):
   numero = input("\nValor Invalido! Ingrese un número: ")
print("\nEl valor es correcto!\nValor ingresado: ",numero)

"""* Escribe un programa que le pida al usuario ingresar un número entre 1 y 10 y valide que el valor ingresado esté dentro de ese rango. Si el valor no está dentro del rango, el programa debe solicitar al usuario que ingrese un valor válido."""

numero = input("Ingrese un número entre 1 y 10: ")

while not (numero.replace(".", "", 1).isdigit()):
  numero = input("\nValor invalido, no es un número! Ingrese un número entre 1 y 10: ")

while float(numero) < 1 or float(numero) > 10:
  numero = input("\nValor invalido! Ingrese un número entre 1 y 10: ")

  while not (numero.replace(".", "", 1).isdigit()):
    numero = input("\nValor invalido, no es un número! Ingrese un número entre 1 y 10: ")

print("\nVALOR CORRECTO!\nValor Ingresado: ",numero)

"""* Escribe un programa que le pida al usuario ingresar su edad y su nombre. Si el usuario ingresa una edad no numérica, el programa debe solicitar al usuario que ingrese un valor válido. Si el usuario ingresa un nombre vacío, el programa debe solicitar al usuario que ingrese un nombre válido."""

nombre = input("Ingresar nombre: ")

while nombre == " " or nombre =="":
  nombre = input("\nIngreso un nombre vacio, ingrese nombre correctamente: ")

edad = input("Ingresar edad: ")

while not edad.isdigit():
  edad = input("\nValor incorrecto, ingresar edad correctamente: ")

print("\nVALORES INGRESADOS\nNombre: ",nombre.title(),"\nEdad: ",edad)

"""* Escribir un programa que solicite al usuario ingresar dos números. El programa debe calcular la división del primer número por el segundo número. Si el segundo número es cero, el programa debe mostrar un mensaje de error indicando que la división por cero no está permitida y solicitar al usuario que ingrese un nuevo segundo número. El programa debe seguir solicitando segundos números hasta que el usuario ingrese un número distinto de cero."""

n1 = input("Ingresar 1° número: ")
n2 = input("Ingresar 2° número: ")

while not (n1.replace(".", "", 1).isdigit()):
  n1 = input("\nValor no numerico, ingresar 1° número: ")

while not (n2.replace(".", "", 1).isdigit()):
  n2 = input("\nValor no numerico, ingresar 2° número: ")

while float(n2) == 0:
  n2 = input("\nLa división por cero no está permitida! Ingresar número:")

  while not (n2.replace(".", "", 1).isdigit()):
    n2 = input("\nValor no numerico, ingresar 2° número: ")


print("\nLa división de los números ingresados es: ",round(float(n1)/float(n2),2))

"""# Problema

Escribir un programa que permita al usuario ingresar los nombres y edades de varios estudiantes y calcule el promedio de edad de los estudiantes. El programa debe validar que el usuario ingrese al menos un estudiante y que las edades ingresadas sean números enteros positivos. Si el usuario ingresa un valor inválido, el programa debe solicitar al usuario que ingrese un valor válido. Además se deberá validar que el nombre sea un `str`
"""

# función para validar que la entrada sea un entero positivo
def validar_entero_positivo(valor):
    try:

      if not valor.isdigit():
        raise ValueError("El valor debe ser un entero positivo")
      #Evalua si es numero o contiene un caracter erroneo
      else:
        valor = int(valor)

      if valor < 0:
        raise ValueError("El valor debe ser un entero positivo")
      #Evalua el rango
    except ValueError as e:
      print("\nError:", e)

    return valor


#Empieza Programa

opcion = input("Que desea hacer?\n1) Agregar alumno\n2) Salir\nIngrese opción elegida: ")
while opcion != "1" and opcion !="2":
  print("\nINGRESAR OPCIÓN CORRECTA!")
  opcion = input("Que desea hacer?\n1) Agregar alumno\n2) Salir\nIngrese opción elegida: ")

edades = []
nombres = []
estudiante = 1
#Listas y contador

while opcion == "1":
  nombre = input(f"\nIngresar nombre del estudiante N°{estudiante}: ")

  while not nombre.isalpha(): #Evalua si el nombre esta formado solamente por caracteres alfabeticos
    nombre = input(f"\nDebe ingresar un nombre valido! \nIngresar nombre del estudiante N°{estudiante}: ")

  edad = input(f"Ingresar edad del estudiante N°{estudiante}: ")

  while not isinstance(validar_entero_positivo(edad),int): #Se utiliza la función definida arriba, pero en un bucle para que se vuelva a pedir la edad si la función arroja error
    edad = input(f"Ingresar edad del estudiante N°{estudiante}: ")

  edades.append(int(edad))
  nombres.append(nombre.title())

  print("-----------------------------------------------------------------------")
  opcion = input("Que desea hacer?\n1) Agregar alumno\n2) Salir\nIngrese opción elegida: ")
  while opcion != "1" and opcion !="2":
    print("\nINGRESAR OPCIÓN CORRECTA!")
    opcion = input("Que desea hacer?\n1) Agregar alumno\n2) Salir\nIngrese opción elegida: ")

  if opcion == "1":
    estudiante += 1

#Desde aca solo para mostrar resultados
print("-----------------------------------------------------------------------")

if estudiante == 1:
  print(f"LISTA DE 0 ESTUDIANTES INGRESADOS")
else:
  print(f"LISTA DE {estudiante} ESTUDIANTES INGRESADOS")

x = 0
for i in nombres:
  print(f"{nombres[x]}: {edades[x]} años")
  x+=1

try:
  if len(edades)==0:
    raise ZeroDivisionError("No se ingresó ningún dato de estudiantes.")
  else:
    print(f"\nPROMEDIO DE EDADES: {round(sum(edades)/len(edades))} años")
except ZeroDivisionError as e:
  print(e)

def obtener_edad():

  while True:

    try:
      edad = int(input("Ingrese su edad: "))

      if edad < 0:
        raise ValueError("La edad debe ser un número positivo.")

      if edad == 0:
        raise ZeroDivisionError("No puede ser 0")
      else:
        print(1/edad)
        return edad

    except Exception as e:
      print("Error:", e)
      print("Error:", type(e))

obtener_edad()