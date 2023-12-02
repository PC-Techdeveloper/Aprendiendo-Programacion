# Números enteros: tipo de dato int
# Ejemplo 1:
v = -3
m = v + 8
print(m)

#Ejemplo 2:
z = round(m/2)
# print(z) #2

#Tipo de dato en formato binario, octal o hexadecimal:
decimal = 8
binario = 0b1101
octal = 0o11
hexadecimal = 0xc
# print(decimal)
# print(binario)
# print(octal)
# print(hexadecimal)

#Números de punto flotante:
real = 1.1 + 2.2 #float
3.300000000003 #aproximado a 3.3
# print(round(real,1)) #muestra 1 cifra decimal

#Números complejos:
complejo = 5 + 3j
complejo.real #5.0
complejo.imag #3.0

#Aritmética de los tipos numéricos:
x = 2
a = x**3 #8 elevado a la 3
# print(a)

b = 31
c = b // 4 # 31 divido 4
# print(c)

h = 31.0
g = h / 4
# print(g)

#Datos numéricos: Booleanos (true-false):
a = False
b = True
# print(a)
# print(b)
c = None
# print(c)

#Cadena de caracteres:
saludo1 = 'Hola"Maria"'
saludo2 = 'Hola \'Maria\''
saludo3 = "Hola 'Maria'"
saludo4 = 'Hola'
# print(saludo1)
# print(saludo2)
# print(saludo3)
# print(saludo4)

#Tipos de datos adicionales:
#Secuencias (list y tuple)
#Conjuntos (set)
#Mapas (dict)

#Ejemplos:
lista = [1,2,3,4,5]
tupla = (3,4,5,7,8)
n = len(tupla)
conjunto = set([1,3,1,4])
diccionario = {'a':1,'b':3,'c':8}
# print(lista)
# print(tupla)
# print("La longitud de la tupla es = ",n)
# print(conjunto)
# print(diccionario)

#Identificar el tipo de variable
#type y isinstance
type(5) #int
type(3.14) #float
type('Hola Mundo') #string
isinstance(7,float) #false
isinstance(8,int) #true
isinstance(2,bool) #false
isinstance(False,bool) #true

#Conversión de tipos de datos:
edad = '24'
edad = int(edad)
# print(edad)
edadString = str(edad)
# print(edadString)
flotante = float('18.66')
# print(flotante)
