/*
Los operadores de comparación en Javascript permiten comparar dos valores. Siempre devuelven un valor booleano (true o false)

También existen los operadores >= o <= que permiten comparar si un número es mayor o igual que otro, o si un número es menor o igual que otro.

Para saber si dos valores son iguales podemos usar el operador === o, para saber si son diferentes, el operador !==

JavaScript compará las cadenas de texto según el valor de su código Unicode. (LAS LETRAS MAYÚSCULAS TIENEN UN VALOR MENOR QUE LAS LETRAS MINÚSCULAS)

Boolenos -> true es mayor que false.
*/

5 > 3; // true
5 < 3; // false

5 >= 3; // true
5 >= 5; // true
5 <= 3; // false
5 <= 5; // false

5 === 5; // true
5 !== 3; // false

// EJERCICIO INTERACTIVO
/*Escribe un código que compruebe si 10 es mayor o igual que 9 */
10 >= 9; // true
0 === 0; // true

// COMPARANDO CADENAS DE TEXTO
'JavaScript' === 'JavaScript'; // true
'JavaScript' === 'Java'; // false
'JavaScript' !== 'PHP'; // true
'Estoy aprendiendo JavaScript' === 'Estoy aprendiendo JavaScript'; // true

'Alfa' > 'Beta'; // false
'Omega' > 'Beta'; // true
'alfa' > 'Alfa'; // true

// COMPARANDO BOOLEANOS
true === true; // true
true === false; // false
false !== false; // false

true > false // true
false < true // true
true > true // false
false < false // false