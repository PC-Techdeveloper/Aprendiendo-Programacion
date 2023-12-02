#En Python, los tres operadores booleanos son: “and” ( y ), “or “( o ), “not”( no ).
#En general, los elementos nulos o vacíos se consideran False y el resto se consideran True.

#Verificando si un elemento es true o false
elemento1 = bool(0)
# print(elemento1)
elemento2 = bool(0.0)
# print(elemento2)
elemento3 = bool('')
# print(elemento3)
elemento4 = bool(5)
# print(elemento4)
elemento5 = bool(3.2)
# print(elemento5)
elemento6 = bool('STR')
# print(elemento6)

#OPERADORES DE COMPARACIÓN
"""
mayor que --> >
menor que --> <
mayor o igual que --> >=
menor o igual que --> <=
igual --> ==
distinto --> !=

"""
#Ejemplos
comparacion1 = 2 == 3
# print(comparacion1)

comparacion2 = 2 > 1
# print(comparacion2)

comparacion3 = 2 > 8
# print(comparacion3)

comparacion4 = 3 >= 8
# print(comparacion4)

comparacion5 = 8 >= 5
# print(comparacion5)

comparacion6 = 1 <= 2
# print(comparacion6)

comparacion7 = 5 != 6
# print(comparacion7)

#Una sentencia condicional necesita:
"""
- una prueba que sea verdadero o falso
- un código si la prueba sea verdadera
- un código opcional si la prueba es falsa

"""

#CONDICIONALES SIMPLES:

"""
sintáxis: IF

if condición:
    #códidgo
    print(...)
else:
    print(...)

else --> se ejecuta cuando la condición if no es verdadera
else - if --> Permite verificar otra condición del if si no se cumple

"""
#ejemplo con condicional if:
numero = 5
if numero > 4:
    print('El numero es mayor que 4')

#Ejemplo con condicional if - else: 
numero2 = 3
if numero2 > 5:
    print('El numero es mayor que 5')
else:
    print('El numero es menor o igual que 5')

#CONDICIONALES ANIDADAS
"""
- Se usan para evaluar multiples condiciones y manejar situaciones más complejas donde se evaluan condicionales dentro de otra en un mismo bloque de código
- Se logra mediante el uso de if,elif y else

"""
consola = int(input("Digita un número:"))


numero = consola

if numero > 0:

    if numero <= 10:
        print("El número está en el rango del 1 al 10")
    elif numero <= 20:
        print("El número está en el rango del 11 al 20")
    elif numero <= 30:
        
        print("El número está en el rango del 21 al 30")
    else:
        print("El número está fuera de los rangos evaluados")

else:
        print("El número es negativo")