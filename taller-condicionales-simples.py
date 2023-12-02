#TALLER 3: CONDICIONALES SIMPLES EN PYTHON
#AUTOR: JEFFERSON CHAVEZ DIAZ
#FECHA: 16 DE NOVIEMBRE DE 2023
#FICHA: 2834903

from datetime import date
today = date.today()
print('La fecha de hoy es:',today)

# Comparando dos números:
numero1 = int(input('Digita el primer número: '))
numero2 = int(input('Digia el segundo número: '))
if numero1 >= numero2:
    print('El número 1 es mayor que el número 2')
else:
    print('El número 2 es menor que el número 1')
print()


# Elección de una carrera profesional

# Mensaje de bienvenida
print('BIENVENIDO A LA SELECCIÓN DE CARRERAS PROFESIONALES: ')
print('Por favor, elige entre las siguientes opciones: ')
print('1) Ingeniería Informática')
print('2) Administración de Empresas')
print()

# Obtener la elección del usuario:
opcion = input('Ingresa el número de la carrera que deseas (1 o 2): ')

# Verificar la elección e imprimir un mensaje correspondiente:
if opcion == '1':
    print("Has escogido la carrera de Ingeniería Informática. ¡Excelente elección!")
elif opcion == '2':
    print("Has escogido la carrera de Administración de Empresas. ¡Buena elección!")
else:
    print("Opción no válida. Por favor, selecciona 1 o 2 para elegir una carrera.")
print()
print('*** Final del Análisis del Programa de Formación SENA en PYTHON ***')
print()


# Conocer la cantidad de caracteres de un string:
jugador = input('Escribe un jugador de futbol que te guste: ')
# Convirtiendo a mayúscula el string:
print('La frase en mayúscula es:',jugador.upper())
longitud = len(jugador)
print('La cantidad de caracteres es:', len(jugador))
if longitud > 10:
    print('La frase contiene más de 10 caracteres')
else: 
    print('La frase contiene menos de 11 caracteres')
print()
print('FIN del programa')