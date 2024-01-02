/*
ARRAYS: Es una colección de elementos.
*/

// DECLARACIÓN Y ASIGNACIÓN DE UN ARRAY
[1, 2, 3, 4, 5];

// Pueden ser cualquier tipo de dato
[1, 2, (3)[(4, 5, 6)], true, 3.14, 'Hola'];

// Asignar un array a una variable
const numeros = [1, 2, 3, 4, 5];
let nombres = ['Diego', 'Felipe', 'Juliana'];

// Acceso a los elementos de un array
console.log(numeros[0]);
// Acceso a un array que NO existe -> undefined
console.log(numeros[10]);

// Utilizar variables para acceder a un array
const numbers = [6, 7, 8, 9];
let index = 2;
console.log(numbers[index]);

// MODIFICAR ELEMENTOS DE UN ARRAY
const numeros2 = [1, 2, 3, 4, 5];
numeros2[0] = 50;
console.log(numeros2); // [50,2,3,4,5]

