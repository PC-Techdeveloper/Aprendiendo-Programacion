/*
Sirven para evaluar expresiones lógicas.

El operador lógico AND se indica con &&. Devuelve true cuando ambos valores que conecta son true.

El operador lógico OR se indica con || y devuelve true cuando cualquiera de los valores que conecta es true.

El operador lógico NOT se indica con ! e invierte el valor de un valor booleano. Se pone delante del valor invertido.
 */

//  OPERADOR LÓGICO AND (&&)
true && true; // true
true && false; // false
false && false; // false

// OPERADOR LÓGICO OR (||)
true || true; // true
true || false; // true
false || false; // false

// OPERADOR LÓGICO NOT (!)
!true; // false
!false; // true

// COMBINANDO OPERADORES LÓGICOS, ARITMÉTICOS Y DE COMPARACIÓN
2 < 3 && 3 < 4; // true

// usar paréntesis para agrupar operaciones y usar operadores lógicos y aritméticos.

(2 + 2) < 3 && (10 < (8 * 2)); // false

// EJERCICIO
// Comprueba si 7 es mayor que 8 y menor que 10
7 > 8 && 7 < 10 // true

/*Tenemos un producto en una tienda. Cuesta 1500 y tenemos un descuento del 25%. Tengo 1150€ en mi cartera. Escribe un código que me diga si puedo comprarlo. No uses paréntesis. */

const producto = 1500 * 0.75 <= 1150;
console.log(producto);

// Dos o más operandos
true && true && true // true

// Mezclar operadores lógicos
true && true || false // true
!true && !true // false
false && true || !true // false