/*
confirm: Muestra un cuadro de dialógo con dos botones 'Aceptar'y 'Cancelar'. Sí el usuario pulsa aceptar, la función devuelve un true. Sí pulsa cancelar devuelve un false.

El bucle do while siempre se ejecutará al menos una vez.
*/

// USANDO DO WHILE
let count = 15;
do {
  count = count - 1;
  console.log(count);
} while (count > 10);

// CONFIRM
do {
  resultado = confirm('¿Quieres decirme algo?');
} while (resultado);
