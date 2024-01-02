/*Estos métodos incluyen indexOf, some, every, find, findIndex e includes.*/

const emojis = ['🍇', '🍌', '🍎'];

// indexOf -> En que posición está el elemento -> SI NO EXISTE, RETORNA -1.
const posicionUva = emojis.indexOf('🍇');
console.log(posicionUva);

// Includes -> El elemento existe en un array -> TRUE O FALSE -> También funciona con las cadenas de texto.
const existeUva = emojis.includes('🍇');
console.log(existeUva);

// some -> Alguno de los elementos cumple con la condición -> Recibe una función como argumento y retorna un valor booleano -> TRUE O FALSE.
const tieneUva = emojis.some((emoji) => emoji === '🍇');
console.log(tieneUva);
// Ejemplo usando some con string
const nombres = ['Pedro', 'Fernando', 'Maria'];
const tieneNombreLargo = nombres.some((names) => names.length > 3);
console.log(tieneNombreLargo);

// Ejemplo usando some con numeros
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
const tieneNumeroMayorA5 = numbers.some((number) => {
  console.log(`Estoy iterando sobre el número ${number}`);
  return number > 5;
});

console.log(tieneNumeroMayorA5);

// every -> Todos los elementos cumplen con la condición, recibe una función como argumento y retorna un valor booleano -> TRUE O FALSE.
/*Al igual que some, el método every deja de iterar sobre el Array en cuanto encuentra un elemento que no cumple con la condición. */
const fruits = ['🍞', '🧀', '🍎', '🍐'];
const tieneTodasLasFrutas = fruits.every((frutas) => frutas === '🍐');
console.log(tieneTodasLasFrutas);

// find -> El método find te permite encontrar el primer elemento que cumple con una condición. Lo interesante es que este método te devuelve el elemento en sí, no un valor booleano como some y every. Aunque el funcionamiento es igual: hay que pasarle una función como argumento que retorne un valor booleano. -> SI NO ENCUENTRA UN ELEMENTO RETORNA UNDEFINED
/*Igual que some y every, el método find deja de iterar sobre el Array en cuanto encuentra un elemento que cumple con la condición. */
const numbers2 = [12, 45, 67, -34];
const primerNumeroNegativo = numbers2.find((number) => number < 0);
console.log(primerNumeroNegativo);

// findIndex -> Devuelve el índice del primer elemento que cumple con la condición -> SI NO ENCUENTRA RETORNA -1
const numbers3 = [34, 12, 67, 98, -11];
const primerNumeroNegativo2 = numbers3.findIndex((number) => number < 0);
console.log(primerNumeroNegativo2);
