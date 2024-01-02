/*CONDICIONAL IF

El código condicional es un bloque de código que se ejecuta sólo si se cumple una condición. En JavaScript usamos la palabra reservada if para crear un bloque condicional.

*/

// IF: Si la condición es true
const edad = 18;
if (edad >= 18) {
  console.log('Eres mayor de edad!');
}

// ELSE: Si la condición es false.
const edad2 = 18;
if (edad2 >= 18) {
  console.log('Eres mayor de edad!');
} else {
  console.log('Eres menor de edad!');
}

// ELSE IF: Comprobar más de una condición.

const edad3 = 18;
if (edad3 >= 18) {
  console.log('Eres mayor de edad');
} else if (edad3 >= 16) {
  console.log('Eres casi mayor de edad');
} else {
  console.log('Eres menor de edad');
}

// ANIDACIÓN DE CONDICIONALES: MUY POCO RECOMENDABLE USAR
const edad4 = 17;
const tienesCarnet = true;

if (edad4 >= 18) {
  if (tienesCarnet) {
    console.log('Puedes conducir!');
  } else {
    console.log('No puedes conducir!');
  }
} else {
  console.log('No puedes conducir, espera que seas mayor de edad!');
}

// USANDO OPERADORES LÓGICOS
const edad5 = 17;
const tienesCarnet2 = true;

if (edad5 >= 18 && tienesCarnet) {
  console.log('PUEDES CONDUCIR UN AUTO!');
} else {
  console.log('NO PUEDES CONDUCIR UN AUTO!');
}

// TÉCNICA INTERESANTE
const edad6 = 17;
const tienesCarnet3 = true;
const puedesConducir = edad >= 18 && tienesCarnet3;

if (puedesConducir) {
  console.log('Puedes conducir!');
} else {
  console.log('No puedes conducir');
}

