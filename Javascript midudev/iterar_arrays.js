// While -> Ejecutá una vez si la condición es true
let frutas = ['🍎', '🍐', '🍉'];
let i = 0; // Como index

while (i < frutas.length) {
  console.log(frutas[i]);
  i++; // Incrementar en 1
}

// for -> Ejecutá la cantidad de veces necesarias.
for (let i = 0; i < frutas.length; i++) {
  console.log(frutas[i]);
}
// Inverso
for (let i = frutas.length - 1; i >= 0; i--) {
  console.log(frutas[i]);
}

// BUCLE FOR...OF -> CUANDO SOLO SE NECESITAN LOS VALORES DE UN ARRAY
let frutas2 = ['🍌', '🍇', '🍊'];
for (const fruta of frutas2) {
  console.log(fruta);
}

// MÉTODO DE ARRAY -> forEach -> SIN BREAK Y INDEX
frutas2.forEach((frutas) => {
  console.log(frutas);
});
