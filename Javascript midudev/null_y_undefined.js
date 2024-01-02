/*
La particularidad de estos dos tipos de datos es que cada uno sólo tiene un valor. El tipo null sólo puede tener el valor null y undefinedsólo puede tener el valor undefined.

DIFERENCIAS:
Mientras que null es un valor que signifca que algo NO TIENE VALOR, undefined significa que algo NO HA SIDO DEFINIDO.
*/

let rolloDePapel;
console.log(rolloDePapel); // undefined

// Asignar directamente el valor undefined a una variable
let rollo_de_papel = undefined;
console.log(rollo_de_papel);

// Para el valor null, lo conseguimos asignandole explícitamente ese valor:
const ROLLO_DE_PAPEL = null;
console.log(ROLLO_DE_PAPEL);

// EJERCICIO
// Crea una variable con let llamada capacidad y asígnale un valor null
let capacidad = null;

// Crea una variable con let llamada dinero y asegúrate que tenga un valor de undefined
let dinero = undefined;

// COMPARACIONES CON NULL Y UNDEFINED

null === undefined // false
null === null // true
undefined === undefined // true