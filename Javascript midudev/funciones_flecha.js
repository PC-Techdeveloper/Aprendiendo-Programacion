/*También conocidas como arrow function 

Las funciones flecha son una forma más concisa de crear funciones en JavaScript, y se han vuelto muy populares en los últimos años debido a su sintaxis simplificada.
*/

const sayHi = () => {
  console.log('Hola');
};
sayHi();

/*
Ventajas de las funciones flecha:

Las funciones flecha tienen varias ventajas sobre las funciones regulares en JavaScript. Algunas son:

Sintaxis más concisa: la sintaxis de las funciones flecha es más corta y más fácil de leer que la sintaxis de las funciones regulares, especialmente cuando se trabaja con funciones de una sola línea.

Return implícito: las funciones flecha puede devolver el valor de la expresión sin usar la palabra clave return cuando son de una sola línea. Esto hace que las funciones flecha sean aún más cortas y más fáciles de leer.

Funciones anónimas más legibles: las funciones flecha son una forma más legible y concisa de crear funciones anónimas en JavaScript, lo cual puede hacer que nuestro código sea más fácil de entender.
*/

// RETURN IMPLÍCITO
/*Cuando una función flecha tiene una sola expresión, podemos omitir las llaves {} y la palabra clave return para hacerla aún más corta. Esto se conoce como return implícito. */

// Declaración de una función regular
function dividir(a, b) {
  return a / b;
}

// Con una función de tipo flecha
const dividiendo = (a, b) => {
  return a / b;
};

// Función flecha con return implícito: Cuando son funciones de una sola línea.
const divide = (a, b) => a / b;
