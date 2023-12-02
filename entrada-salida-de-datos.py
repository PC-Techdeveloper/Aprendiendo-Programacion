#1.1 ENTRADA ESTÁNDAR:
#entrada estandar: input('...')
# edad = input('¿Cuantos años tienes?')

#otra forma de entrada de datos
# print('¿Cuál es tu nombre?')
# nombre = input()
# print('Usted',nombre, 'es un aprendiz SENA')

#entrada de dato de tipo int
# celular = int(input('Digita tu número celular:'))

#entrada de dato tipo float (decimal)
# estatura = float(input('¿Cuál es tu estatura?'))

#1.2 ENTRADA POR SCRIPT
# print('Hola, bienvenido a tu primer script')
# a = input('Digite un nombre: ')
# b = int(input('Digite un numero: '))
# print('Su nombre es: ',a)
# print('Su numero es: ',b)
# c = b**2 #elevado a 2
# print('El valor del numero al cuadrado es: ',c)

#SALIDA DE DATOS

# print('Hola Mundo')
# texto = 'SENA es colombia' #caracteres especiales --> \n: salto de línea, \t: sangrías de texto
# print(texto)

#COLOCAR VARIAS CADENAS DE TEXTO
# print('Hola mundo','Bienvenido a Python','Te encantara este curso')

#2.2 SALIDA DE DATOS CON FORMATO
# % --> operdor de interpolación 
# %c --> un caracter
# %s --> str, cadena de caracteres
# %d --> int, enteros
# %f --> float, flotantes
# %.1f --> salida con 1 decimal
# %.8f --> 8 digitos
# %.2f --> salida con 2 decimales

titulo = 'RAIZ CUADRADA DE TRES'
valor = 3**0.5
print('El resultado de %s es %.1f' % (titulo,valor))
print('Nro. factura: %d, Total: a pagar %f' % (567,12500.83))

#2.3 IMPRESIÓN DE CADENAS

frase1 = ' Perro'
frase2 = ' Gato'
frase3 = ' avestruz'
# + --> concatena cadenas
print(frase1 + frase2 + frase3)
# * --> repite cadenas
print(frase1 * 5)
# cadena.capitalize() --> inicia con mayuscula
print(frase3.capitalize())
# cadena.center(ancho) --> centra en el ancho dado
print(frase1.center(18))
# cadena.lower() --> convierte a minuscula
print(frase1.lower())
# cadena.upper() --> convierte a mayuscula
print(frase1.upper())
# cadena.title() --> mayusculas iniciales
print(frase1.title())

# OPERADORES ARITMÉTICOS
# operadores --> +, -, *, /, %(resiudo o modulo), **, // (devuelve la parte entera del cociente)

# a = 5 + 5
# print(a)
# b = 30 - 10
# print(b)
# c = 200 * 200
# print(c)
# d = 10 / 5
# print(d)
# e = 40 % 12
# print(e)
# f = 5**3
# print(f)
# g = 4 // 3
# print(g)

# 3.3 INICIALIZACIÓN DE VARIABLES
# b = 200
# c = 312 * 2
# print('El resultado de la multiplicacion es:',c)

# 3.4 USO DE CONSTANTES Y VARIABLES

# constantes --> se crean en mayuscula (CONSTANTE1)
IVA = 0.19
precioInicial = 3000
precioFinal = precioInicial * (1.0 + IVA)
print(precioFinal)

# multiples variables en una sola instrucción
a,b,c = 100,200,300
print(a,b,c)

# variable literal --> Un literal es un dato puro, que puede ser un número, una cadena de caracteres o un booleano.

a = 10000
b = a * 2 / 100
c = 'JUAN CARLOS'
print(c,'debe la suma de: $',a+b)

# Se pueden definir varias variables con un mismo dato, así:
a = b = c = 15
print(a)
print(b)
print(c)

# También está permitido, en una sola instrucción, inicializar varias variables con un valor diferente para cada una:
# a,b,c = 200,300,400
# print(a)
# print(b)
# print(c)

# VARIABLES ESPECIALES

# ACUMULADOR --> variable que suma un valor
# suma = suma + edad
# CONTADOR --> sumando/restando un valor constante
# total = total + 1

# 3.5 FUNCIONES PREDEFINIDAS EN PYTHON - TIPOS DE OPERADORES

# FUNCIONES DE CADENA:
# len() --> cantidad de caracteres
# split() --> convierte una cadena en una lista
# lower() --> convierte una cadena en minuscula
# upper() --> convierte una cadena en mayuscula
# replace() --> reemplaza una cadena por otra

# FUNCIONES NÚMERICAS:
# range() --> crea un rango de numeros
# str() --> convierte un valor a texto
# int() --> convierte a un texto a un valor entero
# float() --> convierte a un valor decimal
# max() --> determina el maximo entre un grupo de numeros
# min() --> determina el minimo entre un grupo de numeros
# sum() --> suma el total de una lista de numeros

# OTRAS FUNCIONES:
# list() --> crea una lista a partir de un elemento 
# ord() --> devuelve el valor ASCII de una cadena o caracter
# round() --> redondea despues de la coma de un decimal

# LIBRERIAS DE FECHA, RANDOM, MATEMÁTICAS:

# FECHA --> SI SE NECESITA USAR FECHAS USAR datatime - date 
from datetime import date #fecha-actual
from datetime import datetime #fecha-hora-completa
hoy = date.today()
fecha = datetime.now()
print('La fecha de hoy es:',hoy)
print('La fecha completa de hoy es:',fecha)

# RANDOM --> SI SE REQUIERE NÚMEROS ALEATORIOS 
import random 
a = random.randint(10,100) #numero entero aleatorio entre 10 y 100
print(a)
b = random.randrange(0,100,5) #numero entero aleatorio entre 0 y 100 incrementando en 5
print(b)
c = random.random() #numero decimal aleatorio entre 0.0 y 1.0
print(c)
d = random.uniform(100,200) #numero decimal aleatorio entre 100.0 y 200.0 inclusive
print(d)

# FUNCIONES DE LA LIBRERIA RANDOM
import random
# CHOICE --> permite seleccionar al azar un dato desde un conjunto 
amigos = ['Luis','Mauricio','Fernando','Julian']
ganador = random.choice(amigos)
print('El ganador es:',ganador)
# SUFFLE --> modifica el orden de los elementos de una lista
numeros = [1,2,3,5,6,7,8,9]
random.shuffle(numeros)
print(numeros)
# SAMPLE --> extrae una cantidad de numeros aleatorios a un conjunto
numeros = [23,45,67,88,9,100,200]
random.sample(numeros,3)
print(numeros)

# LIBRERIAS DE MATEMÁTICAS

import math
# trunc() --> Elimina los decimales de un numero float
a = 234.45
b = math.trunc(a)
print(b)

# fabs() --> calcula el valor absoluto de un numero float, eliminando el signo
a = - 200.55
b = math.fabs(a)
print(b)

# factorial() --> solo se usa con numeros enteros, calcula el numero de combinaciones posibles de una serie de objetos, el factorial se expresa como un numero.
a = 6
b = math.factorial(a)
print('El valor factorial de "a", es:',b) #6 = 6x5x4x3x2x1

# fmod() --> calcula el residuo de una division entre dos numeros float
c = math.fmod(16,5)
print('El residuo de dividir 16 entre 5 es:',c)

# sqrt() --> calcula la raiz cuadrada de un numero entero
a = 3
b = math.sqrt(a)
print('La raiz cuadrada de 3 es:',b)

#Las funciones trigonométricas seno, coseno y tangente se realizan usando sin(), cos() y tan().

#Las funciones trigonométricas en la librería math toman los valores de los ángulos expresados como radianes. Por esta razón, debe realizarse la conversión de grados a radianes con la función radians.

#radianes
angulo = 60
radianes = math.radians(angulo)
print('Los radianes son:',radianes)

# #seno
seno = math.sin(radianes)
#coseno
coseno = math.cos(radianes)
# #tangente
tangente = math.tan(radianes)
print('El seno de 60 es:',seno)
print('El coseno de 60 es:',coseno)
print('La tangente de 60 es:',tangente)

























