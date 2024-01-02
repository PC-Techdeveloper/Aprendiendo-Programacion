/*
A la hora de crear programas, es vital poder almacenar información para poder utilizarla en un futuro. En JavaScript se usan las variables para conseguirlo.

Las constantes son variables que no pueden ser reasignadas. Para crear una constante, usamos la palabra reservada const

En JavaScript, también podemos crear variables usando la palabra reservada var. Es la forma más antigua y es normal que encuentres muchos tutoriales que lo usen. Sin embargo, a día de hoy, no es recomendable usar var ya que tiene comportamientos extraños que pueden causar errores en tu código.
*/

let numero = 1;
let result = numero + 1;
console.log(result); // 2

// Reasignar un valor a la variable
numero = 5;
let result2 = numero + 1;
console.log(result2);

// Las variables pueden ser cualquier tipo de dato
let welcomeText = 'Hello World';
let isCool = true;

console.log(welcomeText);
console.log(isCool);

// EJERCICIO
// Crea una variable llamada mensaje y asignale el valor 'Hola JavaScript
let mensaje = 'Hola JavaScript';

// Crea una variable llamada resultado y asiganle la suma de 2 y 3
let numero1 = 2;
let numero2 = 3;
let resultado = numero1 + numero2;
console.log(resultado);

// CONSTANTES
const PI = 3.1416;
// Si se reasigna el valor de la constante dará un ERROR
// ❌ PI = 4

// ✅ let numero
// ❌ const RADIUS -> ERROR DE SINTÁXIS

// EJERCICIO
// Crea una constante llamada IS_DIABLED y asignale el booleano 'true'
const IS_DISABLED = true;

// EL NOMBRE DE LAS VARIABLES
/*En JavaScript, los nombres de las variables pueden contener letras, números y el guión bajo (_). Además, el primer carácter del nombre de la variable no puede ser un número.

Es importante tener en cuenta que los nombres de las variables son sensibles a las mayúsculas y minúsculas, lo que significa que miVariable y mivariable son dos variables diferentes en JavaScript. */

let miVariable = 1;
let mivariable = 2;
let respuesta = miVariable + mivariable;
console.log(respuesta);

/*También es importante que los nombres de las variables sean descriptivos. Por ejemplo, si queremos almacenar el nombre de un usuario, podemos llamar a la variable userName.  */

let n = 'Pepe'; // ❌ NO ES DESCRIPTIVO
let userName = 'Juan'; // ✅ ES ENTENDIBLE.

// CONVENCIONES Y NOMENCLATURAS
/*En JavaScript, existen diferentes nomenclaturas para nombrar las variables: camelCase, snake_case y SCREAMING_CASE.

camelCase es la forma más común de nombrar las variables en JavaScript. Consiste en escribir la primera palabra en minúsculas y las siguientes palabras con su primera letra en mayúsculas. */

let camelCase = 1;
let CamelCaseIsCool = 2;
let userName2 = 'MIDUDEV';

/*snake_case es una forma de nombrar que consiste en escribir todas las palabras en minúsculas y separarlas con guiones bajos. IDEAL USARLO AL CREAR LOS FICHEROS O ARCHIVOS DE JAVASCRIPT*/

let snake_case = 1;
let snake_case_is_cool = true;
let user_name = 'JEFFERSON';

/*SCREAMING_CASE es una forma de nombrar que consiste en escribir todas las palabras en mayúsculas y separarlas con guiones bajos. PARA LAS CONSTANTES ES COMÚN USAR SCREAMING_CASE */

const SCREAMING_CASE = 1;
const SCREAMING_CASE_IS_COOL = false;
const USER_NAME = 'SARAH';
