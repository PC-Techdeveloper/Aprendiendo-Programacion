# ciclos iterativos con python
"""
los dos tipos principales de ciclos iterativos en python son 
'for' y 'while'

"""

# ciclo for:
"""
itera una secuencia -> lista,tupla,diccionario,conjunto o una cadena

"""
# ejemplo:
# fruta = ['Pera','Manzana','Sandia','Uva']
# for fruta in fruta:
#     print(fruta)

# ciclo while:
"""
ejecuta un bloque de código mientras se cumpla una condición específica

"""
# ejemplo:
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1 

# Uso del range ():
"""
uso de range -> indicar un rango de valores, puede tomar uno, dos o tres
argumentos y se usa comunmente en bucles 'for'

SINTAXIS:
range(incio, fin, paso)

inicio -> Valor inicial del rango (por defcto 0)
fin -> Valor final del rango (no incluye en la secuencia generada)
paso -> El incremento entre cada número en el rango (por defecto 1 si no se especifica)

"""
#ejemplo1 -> si solo se proporciona 'range(fin)', 'inicio' se asume como un 0 y genera secuencia desde 0 hasta 'fin' - 1
# for i in range(5):
    # print(i) # 0,1,2,3,4

# parte 2 -> si se proporciona 2 argumentos range(inicio,fin), genera una secuencia desde 'inicio' hasta 'fin' - 1
# for i in range(2,8):
#     print(i) # 2,3,4,5,6,7

# parte 3 -> El paso es el valor de incremento entre cada número en la secuencia.
# for i in range(1,10,2):
#     print(i) # 1,3,5,7,9

# Tambien se puede usar range() para crear una lista de números:
# listaNumeros = list(range(5,15,2))
# print(listaNumeros)
"""
'break' -> cuando finaliza un código
'continue' --> continua un código ignorando el resto del código
"""
# ejemplo:
# for numero in range(10):
#     if numero == 5:
#         continue #break
#     print(numero)

# else con ciclos:
"""
En python también se puede utilzar else que se ejecuta
al funal del ciclo si no se ha activado ninguna declaracion 'break'
"""
#ejemplo 
# for numero in range(5):
#     print(numero)
# else:
#     print('El ciclo ha terminado')

# 1.3 -> USO Y ESTRUCTURA:
"""
La sentencia for se puede usar para imprimir cadenas, listas, tuplas, conjuntos o diccionarios.
"""
#ejemplo:
# for letra in 'HOLA MUNDO':
#     print(letra)
# print('FIN DEL CICLO')

# ITERAR A TRAVÉS DE UNA LISTA -> Recorrer elementos
# miLista = [1,2,3,4,5]
# for elemento in miLista:
#     print(elemento) # 1,2,3,4,5

# USAR EL INDICE Y EL ELEMENTO -> Usar 'enumerate()' junto con el bucle 'for'
# 'enuemrate()' -> Asigna un número de indice a cada elemento de la lista
# miLista = [1,2,3,4,5]
# for indice,valor in enumerate(miLista):
#     print(f'El elemento en el índice {indice} es {valor}')

# MODIFICAR ELEMENTOS DE UNA LISTA -> cada elemento de la lista 'numeros' se multiplica por 2 utilizando un bucle 'for', la funcion 'len' junto con 'range()' para acceder a los índices.
# numeros = [1,2,3,4,5]
# for i in range(len(numeros)):
#     numeros[i] *= 2
# print(numeros)

# USAR EL BUCLE 'FOR' PARA CONSTRUIR NUEVAS LISTAS BASADAS EN OTRA LISTA -> Se crea una nuevaLista que multiplica por 3 cada elemento de la listaOriginal
# listaOriginal = [1,2,3,4,5]
# nuevaLista = [elemento * 3 for elemento in listaOriginal]
# print(nuevaLista)

# USO DEL BUCLE FOR EN TUPLAS:

# ITERAR A TRAVÉS DE TUPLAS -> Itera cada elemento de la tupla e imprime cada elemento en una línea separada.

# miTupla = (1,2,3,4,5)
# for elemento in miTupla:
#     print(elemento) # 1,2,3,4,5

# USAR EL ÍNDICE Y EL ELEMENTO -> enumerate() asigna un número de índice a cada elemento de la tupla mientras se itera a través de ella.
# miTupla = ('a','b','c','d')
# for indice, valor in enumerate(miTupla):
#     print(f'El elemento en el índice {indice} es {valor}')

# BUCLE FOR PARA CONSTRUIR TUPLAS -> una nueva tupla basada en otra tupla o datos existentes
# miTupla = (2,4,6,8)
#nueva tupla
# nuevaTupla = tuple(elemento * 3 for elemento in miTupla)
# print(nuevaTupla)

#USO DEL BUCLE FOR EN CONJUNTOS -> recorrer elementos de un conjunto
# miConjunto = {1,2,3,4,5}
# for elemento in miConjunto:
#     print(elemento)
# Verificar pertenencia -> si un elemento esta presente en el conjunto
# 
# miConjunto = {'a','b','c','d'}
# elementoBuscar = 'b'
# for elemento in miConjunto:
#     if elemento == elementoBuscar:
#         print(f'{elementoBuscar}'' Si esta presente en el conjunto.')
#         break
# else:
#     print(f'{elementoBuscar}'' No esta presente en el conjunto.')

# USAR BUCLE FOR PARA REALIZAR OPERACIONES EN CONJUNTOS
# mi_conjunto = {10, 20, 30, 40}
# for elemento in mi_conjunto:
#     resultado = elemento ** 2
#     print(f'El cuadrado de {elemento} es {resultado}')

# USO DEL BUCLE FOR EN DICCIONARIOS
"""
Los diccionarios no tienen un orden específico, por lo que las claves se mostrarán en cualquier orden.
"""
# diccionario = {'a':1,'b':2,'c':3,'d':4,'e':5}
# for clave in diccionario:
#     print(clave)

# ITERAR A TRAVÉS DE CLAVES Y VALORES -> usar el método items() para iterar a través de las claves y valores de un diccionario.
# diccionario = {'a':1,'b':2,'c':3,'d':4,'e':5}
# for clave,valor in diccionario.items():
#     print(f'Clave: {clave}, Valor: {valor}')

# VERIFICAR EXISTENCIA DE UNA CLAVE
"""
verificar si una clave esta presente en el diccionario

"""
# diccionario = {'a':1,'b':2,'c':3,'d':4,'e':5,}
# buscarClave = 'e'
# for clave in diccionario:
#     if clave == buscarClave:
#         print(f'{buscarClave} Si esta presente en el diccionario')
#         break
# else:
#     print(f'{buscarClave} No esta presente en el diccionario')

# SENTENCIAS BREAK, CONTINUE Y PASS EN PYTHON
"""
Break -> se utiliza para salir de un bucle sin completar todas las iteraciones
Continue -> se utiliza para omitir el resto del código en el bucle y pasar a la siguiente iteración
Pass -> se utilzia cuando lo requiere pero no se necesita ya que no hace nada
"""
#break
# for a in range(5):
#     if a == 3:
#         break
#     print(a)

#continue
# for b in range(5):
#     if b == 3:
#         continue
#     print(b)

#pass
# for c in range(5):
#     if c == 3:
#         pass
#     print(c)

# ESTRUCTURA FOR - ELSE EN PYTHON
"""
Es una construcción que permite agregar un bloque de código que se ejecute después de un bucle 'for' se completa normalmente, es decir, cuando NO se activa la sentencia 'break' dentro del bucle. La clausula 'else' en un bucle 'for' se ejecuta si el bucle finaliza su iteración natural, es decir, NO es interrumpido por un 'break'

"""
# for i in range(5):
#     if i == 6: #esta condición nunca se cumple por lo tanto se imprime el mensaje
#         break
#     print(i)
# else:
#     print('El bucle for ha terminado de manera normal')

# for i in range(7):
#     if i == 6: #Si cumple la condición
#         break
#     print(i)
# else:
#     print('El bucle for ha terminado de manera normal')

# CICLO WHILE
"""
sintaxis -> while condition:
             código
"""
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
# print('FIN DEL PROGRAMA')

# TIPOS DE BUCLE WHILE
"""
2 tipos de ciclos repetitivos con la sentencia while:
- While controlado por contador.
- While controlado por evento.
"""
# ciclo while por contador:
# contador = 0
# while contador < 5:
#     print(contador)
#     contador += 1
# print('FIN DEL CICLO POR CONTADOR')

# ciclo while por evento:
eventoOcurrido = False
while not eventoOcurrido:
    #verifica si el evento ha ocurrido
    eventoOcurrido = input('Presiona la tecla ENTER para simular un evento') != ''
    #realiza acciones mientras el evento no ha ocurrido
    if not eventoOcurrido:
        print('Esperando evento...')
print('Evento detectado. FIN DEL PROGRAMA');


