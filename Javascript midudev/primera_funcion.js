/*Una función es un bloque de código que realiza una tarea específica cuando se llama. Puedes pensar en una función como en un microondas: le das algo para cocinar, le pasas algunos parámetros (como el tiempo y la potencia) y luego hace su trabajo y te devuelve el resultado.

En JavaScript, las funciones se pueden definir de varias maneras, pero la forma más común y básica es mediante la palabra clave function.  */

function saludar() {
  console.log('Hola!👌 Soy tu primera función');
}

// Invocando a la función
saludar();
saludar();
saludar();

// Retornando un resultado
function sumar() {
  return 1 + 1;
}

// Guardar el resultado en una variable
const sumando = sumar();
// Mostrar directamente el resultado
console.log(sumando);

/* UNA FUNCIÓN ÚTIL
 Math -> un objeto incorporado en JavaScript que tiene propiedades y métodos para constantes y funciones matemáticas. 

random -> Devuelve un número aleatorio entre 0 y 1, con decimales.
floor -> Redondea un número hacia abajo.
*/
function getRandomNumber() {
  const random = Math.random();
  const multiplied = random * 10;
  const rounded = Math.floor(multiplied);
  const result = rounded + 1;

  return result;
}
console.log(getRandomNumber());
console.log(getRandomNumber());
console.log(getRandomNumber());

