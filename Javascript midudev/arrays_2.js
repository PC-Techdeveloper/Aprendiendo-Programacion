/*
MÉTODOS Y PROPIEDADES DE ARRAYS

PROPIEDAD:
length -> Conocer longitud de un array y cortar longitud asignando un nuevo valor a la propiedad.

MÉTODOS DE ARRAYS:

push -> Añadir un elemento al final.
pop -> Elimina y devuelve el ultimo elemento.
shift -> Elimina y devuelve el primer elemento.
unshift -> Añade un elemento al principio.

concat -> Unir arrays.
Otra forma de concatenar arrays es usando el operador (...) (spread operator). Este operador propaga los elementos de un array. 


*/

const fruits = ['Manzana', 'Pera', 'Sandia', 'Piña'];
// Longitud de un array
console.log(fruits.length);
// Cortar longitud
fruits.length = 2;
console.log(fruits); // ['Manzana','Pera']

const marcasAuto = ['Audi', 'Nissan', 'Bmw'];
//push
marcasAuto.push('Toyota');
//pop
marcasAuto.pop();
//shift
marcasAuto.shift();
//unshift
marcasAuto.unshift('Ferrari');
console.log(marcasAuto);

// CONCATENAR ARRAYS -> Usando el método concat
const numbers = [1, 2, 3];
const numbers2 = [4, 5, 6];
const allNumbers = numbers.concat(numbers2);
console.log(allNumbers);
// spread -> ...
const numbers3 = [1, 2, 3];
const numbers4 = [4, 5];
const allNumbers2 = [...numbers3, ...numbers4];
console.log(allNumbers);

// EJERCICIO PRÁCTICO
/*En un restaurante se reciben pedidos de comida a domicilio. Vamos a escribir una función procesarPedido que recibe un pedido, que es un array de platos. Lo que debemos hacer es:

El primer elemento lo sacamos del array, ya que es el nombre del cliente.
Añadimos al principio del array la cadena de texto "bebida", ya que es una promoción que tenemos.
Después añadimos al final del array el nombre del usuario que sacamos antes. */

const platos = ['Miguel', 'Hamburguesa', 'Pizza', 'Perro'];
function procesarPedido(pedidos) {
  pedidos.shift();
  pedidos.unshift('Bebida');
  pedidos.push('Miguel');
  return pedidos;
}
const result = procesarPedido(platos);
console.log(result);
