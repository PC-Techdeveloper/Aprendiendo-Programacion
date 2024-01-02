/*Un bucle es una estructura de control que permite repetir un bloque de instrucciones. 

El bucle while ejecuta una sección de código mientras se cumple una determinada condición.
*/

let cuentaAtras = 10;

while (cuentaAtras > 0) {
  cuentaAtras = cuentaAtras - 1;
  if (cuentaAtras % 2 === 0) {
    // Salir del bucle
    // break;
    // Saltar a la siguiente iteración
    continue;
  }
  console.log(cuentaAtras + ' segundos');
}
console.log('¡Despegue! 🚀');
