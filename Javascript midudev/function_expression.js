/*
Una function expression es una función que se asigna a una variable esto significa que podemos llamar a la función usando el nombre de la variable.
*/

// Esto es una function expression
const mult = function (a, b) {
  return a * b;
};
console.log(mult(3, 3));

// Esto es una declaración de función
function resta(a, b) {
  return a - b;
}
console.log(resta(4, 2));

// HOISTING
/*El hoisting es un término que se usa para describir cómo JavaScript parece que mueve las declaraciones funciones al principio del código, de forma que las puedes usar incluso antes de declararlas.  ❌ ERROR */

// console.log(mult2(5, 3));
// const mult2 = function (a, b) {
//   return a * b;
// };

/*
El hoisting solo se aplica a las declaraciones de función. Las funciones de expresión no se elevan (hoisted) al principio del ámbito, por lo que no se pueden usar antes de ser declaradas. */
