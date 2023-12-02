# EJERCICIOS DE VARIABLES, TIPOS DE DATOS Y OPERADORES:

#1 -> Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1 = 54

#2 -> No borres la variable número uno y crea una variable llamada "numero2" asignándole un número decimal de tu elección.
numero2 = 3.5

#3 -> Crea una variable llamada "suma" y almacena la suma de "numero1" más "numero2".
suma = numero1 + numero2

#4 -> Ahora crea tres variables más sin borrar lo que tienes. Una para resta, otra para multiplicación y otra para división. Quiero que me hagas todas estas operaciones al igual que has hecho con la suma y después las imprimes todas.
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(suma,resta,multiplicacion,division)

#5 -> Crea una variable llamada "nombre" y asignale tu nombre como valor.
nombre = 'Jefferson'
#6 -> Crea una variable llamada "precio" y asignale un valor decimal que represente el precio de un artículo ficticio.
precio = 10.99

#7 -> Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asignale un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al 100% y el valor 0 al 0%.
descuento = 0.15

#8 -> Ahora, intenta calcular el precio final aplicando el descuento al precio original y almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que aplicar la lógica de matemáticas. Como pista te voy a decir que para sacar el descuento de un precio, primero tienes que multiplicar el precio original (en este caso 10.99), por el precio de descuento. Después de esta operación le restamos al precio (que sería 10.99 en mi ejemplo) lo que nos haya dado esa primera operación.
precioFinal = precio - (precio * descuento)
print(precioFinal)

#9 -> Crea una variable llamada "cadena" y le asignas un texto, una frase, lo que quieras de tu elección. Qué sea un string.
cadena = 'Hola, Bienvenido a Python'

#10 -> Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de Python.
longitud = len(cadena)
print(f'La longitud de caracteres es: {longitud} letras')

#11 -> Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y este quiero que lo conviertas a número entero. Lo puedes hacer en la misma variable o en otra, da lo mismo.
precio = 34.55
precioEntero = int(precio)
print(precioEntero) # salida -> 34

# 12 -> Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" con ellas quiero que me concatenes en una tercera variable llamada "nombre_completo", el nombre y el apellido con un espacio entre medio. Puedes usar libremente la forma de concatenación que quieras.
nombre = 'Jefferson'
apellido = 'Chavez Diaz'
nombreCompleto = (f'{nombre} {apellido}')
print(nombreCompleto)

#13 -> Escribe nuevamente tu edad en una variable. Después, en otra línea, quiero que le hagas un incremento en 1. Dicho incremento, no hace falta que lo guardes en otra variable. Aunque lo puedes hacer, si quieres.
edad = 24
if edad == 24:
    edad += 1
    print(f'Tu edad es: {edad} años')

#14 -> Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y centímetros. Por ejemplo: 1.83. Después, quiero que a este valor le decrementes el valor 0.1 al valor de la altura.
altura = 1.86
altura -= 0.1
print(f'Tu altura es: {altura} metros')

#15 -> Esta vez, crea una variable que contenga tu nombre completamente en mayúsculas. Después quiero que lo transformes todo en minúsculas con algún método o función de Python.
miNombre = 'jefferson chavez diaz'
nombreMayuscula = miNombre.upper()
nombreMinuscula = miNombre.lower()
print(nombreMayuscula,nombreMinuscula)

#16 -> Por último, con la variable con el nombre en mayúsculas, quiero que le apliques un método parecido para que se transforme todo en minúsculas excepto la primera letra.
nombreModificado = miNombre.capitalize() # Primer letra en Mayúscula (j).
print(f'Tu primer letra a mayúscula es: {nombreModificado}')