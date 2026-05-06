// Las variables en javascript tienen una particularidad, se pueden declarar para una sola parte del codigo
// osea el codigo esta dividido en bloques a esto se le llama scope 
// hay 3 tipos pricipales de variables, var, let y const

// var es un tipo de variable que puede ser usada globalmente por todo el codigo

var saludo = 'hola';

// let es una variable que solo puede ser usada en su scope, para el resto del codigo no es valida

let numerin = 69;

// const es un tipo de varible constante o inmutable tambien de scope global

const tablos = escencia;

// Las variables tambien se pueden declarar juntas con la , pero no es recomendable porque dificulta la lectura del codigo

let a = 1, b = 2, c = 3;

// otro concepto importante en js es el hoisting, en el cual aveces una variable puede ser llamada antes de ser definida 
// Pero se tiende a primero declarar las variables antes de usarlas para evitar confusiones, errores de codigo y facilital la lectura del mismo
// Esto solo aplica para var y no para let y const

