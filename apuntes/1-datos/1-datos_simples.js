// Tipos de datos:

//==============================================
//
//        DATOS SIMPLES
//
//==============================================

// COMENTARIOS
// se escriben con //

// STRINGS
// Se escribe entre " " o ' ', soporta escribir en varias lineas a la ves

let string = 'Esto es un string';

// NUMBER
// Se escriben tal cual en la variable

let number = 17;

// BOLEANO
// Valores de verdadero o falso, tambien se escriben tal cual pero el programa los detecta

let verdad = true;

// Al final de cada linea se debe agregar un ; para indicar a js que la linea acaba ahi, no es obligatorio
// pero si una buena practica

//==============================================
//
//         DATOS ESPECIALES
//
//==============================================

// undefined
// significa que una variable fue declara pero que no tiene ningun valor asociado

let x;
console.log(x); // undefined

// null
// significa que la variable fue declarada con un valor vacio, a diferencia de undifined esta es a proposito

let usuario = null;

// NaN
// Not a Number significa que se esta intentando operar con valores incompatibles, ejemplo un string y un number

let resultado = "hola" * 2;
console.log(resultado); // NaN