/*El operador typeof devuelve una cadena de texto que indica el tipo de un operando. Puede ser usado con cualquier tipo de operando, incluyendo variables y literales.*/

const MAGIC_NUMBER = 7;
console.log(typeof MAGIC_NUMBER); // number

// Valores a comprobar
console.log(typeof undefined);
console.log(typeof true);
console.log(typeof 42);
console.log(typeof 'Hola Mundo');

// EJERCICIO
/*Tengo una variable llamada userName. Escribe el código necesario para ver su tipo */
console.log(typeof userName);

/* Existe, sin embargo, un valor especial en JavaScript, null, que es considerado un bug en el lenguaje. El operador typeof devuelve "object" cuando se usa con null: */
console.log(typeof null);

// Comprobar si una variable es null, usar la comparación estricta (===).
const foo = null;
console.log(foo === null); // true

// USANDO OPERADORES DE COMPARACIÓN
const AGE = 42;
console.log(typeof AGE === 'number'); // true

const MY_AGE = 24;
console.log(typeof MY_AGE === 'number' && AGE > 18); // true

// EJERCICIO
/*Tengo una variable llamada dogId pero no tengo claro si es una cadena de texto. Escribe el código necesario para asegurarte */
console.log(typeof dogId === 'string');
