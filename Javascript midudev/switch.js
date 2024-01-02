/*En JavaScript, la sentencia switch es una estructura de control que nos permite ejecutar diferentes bloques de código dependiendo del valor de una expresión. Esta estructura es útil cuando queremos realizar diferentes acciones basadas en una única variable. */

// Mostrar un mensaje diferente dependiendo del día de la semana.
const day = 'lunes';

switch (day) {
  case 'lunes':
    console.log('Hoy es lunes!😅');
    break;
  default:
    console.log('No es lunes, YAV!🚀');
    break;
}

/* 
Recuperar información de la hora y la fecha -> Objeto Date.
Este objeto tiene un método llamado getDay() -> Devuelve el día de la semana en formato numérico, siendo 0 (domingo) y 6 (sabado)
*/

const dia = new Date().getDate();

switch (dia) {
  case 0:
    console.log('Hoy es domingo!');
    break;
  case 1:
    console.log('lunes');
    break;
  case 2:
    console.log('martes');
    break;
  case 3:
    console.log('miercoles');
    break;
  default:
    console.log('Se acerca el fin de semana');
}

// SWITHC VS IF -> El mismo código en un if - else if.

// AGRUPANDO CASES
switch (dia) {
  case 0:
  case 6:
    console.log('¡Hoy es fin de semana! 🥳');
    break;
  case 1:
  case 2:
  case 3:
  case 4:
    console.log('¡Nooo, a trabajar! 😢');
    break;
  case 5:
    console.log('¡Hoy es viernes! 🤓');
    break;
}
