#TALLER 5 DE PYTHON -> CICLO FOR
#AUTOR: JANER JAEZ
#FECHA: 1 de Diciembre de 2023

from datetime import date
hoy = date.today()
print('El dia de hoy es:',hoy)

print('TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR:')
print('MOSTRANDO UNA LISTA DE FRUTAS:')
fruta1 = input('Escribe una fruta: ')
fruta2 = input('Escribe una segunda fruta: ')
fruta3 = input('Escribe una tercer fruta: ')
fruta4 = input('Escribe una cuarta fruta: ')
fruta5 = input('Escribe una quinta fruta: ')
print('Las frutas que has escrito son:')
for frutas in fruta1,fruta2,fruta3,fruta4,fruta5:
    print(frutas.capitalize())
print('FIN DEL CICLO')
#------------------------------------------------------------
print('¿CUÁL ES EL NÚMERO MÁS GRANDE?')
#Pedimos al usuario que ingrese los números a comparar:
cantidadNumeros = int(input('Por favor, digita la cantidad de números que deseas comparar: '))
#Creando la variable para guardar el número más grande:
numeroGrande = float('-inf')
#Ciclo for
for numeros in range(cantidadNumeros):
    numero = int(input(f'Ingresa el número {numeros + 1}: '))
    if numero > numeroGrande:
        numeroGrande = numero
print(f'El número más grande es: {numeroGrande}')
print('FIN DEL CICLO')
#------------------------------------------------------------
print('CONTEO DE NÚMEROS:')
number = int(input('Escribe el número: '))
for num in range(number):
    print(num)
#------------------------------------------------------------
print('CONVIERTIENDO UN STRING A MAYÚSCULA:')
empresa = input('Digite el nombre de una empresa: ')
empresa = empresa.upper()
for character in empresa:
    print(character)
print('FIN DEL CICLO')

print('FIN DEL PROGRAMA')



