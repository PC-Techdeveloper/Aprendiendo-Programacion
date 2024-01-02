/*La recursividad es una técnica de programación que consiste en que una función se llame a sí misma. Pero no se sabe cuando termina, para eso se evita con una condición base*/

function cuentaAtras(numero) {
  // Condición base: Si el número es menor que 0, sale de la función
  if (numero < 0) {
    return;
  }
  // Si es mayor o igual 0, lo muestra
  console.log(numero);
  // Llamar a la función con el número anterior
  cuentaAtras(numero - 1);
}

cuentaAtras(3);

/*
USANDO RECURSIVIDAD Y DEVOLVIENDO UN NÚMERO
La recursividad se usa muchas veces para solucionar algoritmos. 
*/

// Calculando el factorial de un número
function factorial(n) {
  // Condición base: Si el número es 0 o 1, devuelve 1... Y no se llama a la función de nuevo
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(3));
console.log(factorial(6));

// EJERCICIO
// La función recursiva se llama 3 veces (1 + 2 + 3)
function recursive(n) {
  if (n === 0) {
    return 0;
  } else {
    return n + recursive(n - 1);
  }
}
console.log(recursive(3));
