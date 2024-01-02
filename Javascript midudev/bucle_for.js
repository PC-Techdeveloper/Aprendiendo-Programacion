/*
La estructura de control for en JavaScript es muy útil para ejecutar una serie de instrucciones un número determinado de veces. A diferencia de while que usa una condición para determinar si se ejecuta o no el bloque de código, for usa un contador que se incrementa en cada iteración hasta que se cumple una condición.
*/

// Imprimir los números del 1 al 10
for (let number = 1; number <= 10; number++) {
  console.log(number);
}

// Iterando al revés
for (let i = 10; i >= 0; i--) {
  if (i === 5) {
    console.log('Despegue!🚀');
  } else {
    console.log(`Faltan ${i} segundos.`);
  }
}

// Variables a la vez -> (coma)
for (let i = 0, j = 5; i < 5; i++, j--) {
  console.log(i, j);
}

// Continue y break
for (let i = 0; i < 10; i++){
  const esPar = 1 % 2 === 0
  if (esPar) {
    continue;
  }
  // Si es impar
  console.log(i);
  if (i === 7) {
    // Sale del bucle al llegar a 7
    break;
  }
}